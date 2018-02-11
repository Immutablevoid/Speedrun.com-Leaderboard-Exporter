using System;

namespace SLE
{
	internal sealed class TimeFormat
	{
		public string displayFormat(double sec, double deci)
		{

			bool DisplaySecs = Properties.Settings.Default.DisplaySeconds;

			string str = String.Empty;

			if (DisplaySecs == false)
			{
				TimeSpan time = TimeSpan.FromSeconds(sec);
				if (sec >= 3600)
				{
					if (deci == 0)
					{
						str = time.ToString(@"h\h\:mm\m\i\n\:ss\s\e\c");
					}
					else
					{
						str = time.ToString(@"h\h\:mm\m\i\n\:ss\s\e\c\:") + deci.ToString() + "ms";
					}
				}
				else if (sec >= 60 && sec < 3600)
				{
					if (deci == 0)
					{
						str = time.ToString(@"m\m\i\n\:ss\s\e\c");
					}
					else
					{
						str = time.ToString(@"m\m\i\n\:ss\s\e\c\:") + deci.ToString() + "ms";
					}
				}
				else
				{
					if (deci == 0)
					{
						str = time.ToString(@"ss\s\e\c");
					}
					else
					{
						str = time.ToString(@"ss\s\e\c\:") + deci.ToString() + "ms";
					}
				}
			}
			else
			{
				str = sec.ToString();
			}
			return str;
		}

		public string exportFormat(double sec, double deci)
		{

			bool DisplaySecs = Properties.Settings.Default.DisplaySeconds;

			string str = String.Empty;

			if (DisplaySecs == false)
			{
				TimeSpan time = TimeSpan.FromSeconds(sec);
				if (sec >= 3600)
				{
					if (deci == 0)
					{
						str = time.ToString(@"h\h\:mm\m\i\n\:ss\s\e\c");
					}
					else
					{
						str = time.ToString(@"h\h\:mm\m\i\n\:ss\s\e\c\:") + deci.ToString() + "ms";
					}
				}
				else if (sec >= 60 && sec < 3600)
				{
					if (deci == 0)
					{
						str = time.ToString(@"m\m\i\n\:ss\s\e\c");
					}
					else
					{
						str = time.ToString(@"m\m\i\n\:ss\s\e\c\:") + deci.ToString() + "ms";
					}
				}
				else
				{
					if (deci == 0)
					{
						str = time.ToString(@"ss\s\e\c");
					}
					else
					{
						str = time.ToString(@"ss\s\e\c\:") + deci.ToString() + "ms";
					}
				}
			}
			else
			{
				str = sec.ToString();
			}
			return str;
		}

		public string generalFormat(double sec, double deci)
		{

			string str = String.Empty;

			TimeSpan time = TimeSpan.FromSeconds(sec);
			if (sec >= 3600)
			{
				if (deci == 0)
				{
					str = time.ToString(@"h\h\:mm\m\i\n\:ss\s\e\c");
				}
				else
				{
					str = time.ToString(@"h\h\:mm\m\i\n\:ss\s\e\c\:") + deci.ToString() + "ms";
				}
			}
			else if (sec >= 60 && sec < 3600)
			{
				if (deci == 0)
				{
					str = time.ToString(@"m\m\i\n\:ss\s\e\c");
				}
				else
				{
					str = time.ToString(@"m\m\i\n\:ss\s\e\c\:") + deci.ToString() + "ms";
				}
			}
			else
			{
				if (deci == 0)
				{
					str = time.ToString(@"ss\s\e\c");
				}
				else
				{
					str = time.ToString(@"ss\s\e\c\:") + deci.ToString() + "ms";
				}
			}

			return str;
		}
	}
}
