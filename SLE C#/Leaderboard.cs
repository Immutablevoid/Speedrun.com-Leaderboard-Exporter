using System.Collections.Generic;
using System.Linq;
using System.Net;
using Newtonsoft.Json;
using RestSharp;
using SLE;
using SLEAPI.Internal;

namespace SLEAPI
{
	public sealed class Leaderboard
	{
		public IList<LeaderboardRun> Get(string game, string category)
		{
			var client = new RestClient("https://www.speedrun.com");
			var request = new RestRequest($"/api/v1/leaderboards/{game}/category/{category}", Method.GET);

			var response = client.Execute(request);

			var content = response.Content;
			var runData = JsonConvert.DeserializeObject<RunData>(content);


			return (from run in runData.data.runs.AsParallel()
					let names = GetPlayers(run.run.players)
					select new LeaderboardRun(run.place, run.run.times.primary_t, names)).ToList();
		}

		public void Get(string game, string category, string level)
		{
			// this would be for the other API call
		}

		private IList<string> GetPlayers(IList<PlayerMetadata> players)
		{
			return (from player in players
					select player.id != null ? GetPlayer(player) : player.name).ToList();
		}

		private string GetPlayer(PlayerMetadata player)
		{
			var client = new RestClient("https://www.speedrun.com");
			var request = new RestRequest(player.uri, Method.GET);

			var response = client.Execute(request);

			var content = response.Content;
			var userData = JsonConvert.DeserializeObject<UserData>(content);

			return response.StatusCode == HttpStatusCode.OK ? userData.data.names.international : "Unknown";
		}
	}
}

