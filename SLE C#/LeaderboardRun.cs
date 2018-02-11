using System.Collections.Generic;

namespace SLE
{
  public sealed class LeaderboardRun
  {
    public int Place { get; }
    public decimal RunSeconds { get; }
    public IList<string> Players { get; }

    public LeaderboardRun(int place, decimal runSeconds, IList<string> players)
    {
      Place = place;
      RunSeconds = runSeconds;
      Players = players;
    }
  }
}