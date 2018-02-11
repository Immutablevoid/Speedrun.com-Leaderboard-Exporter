using System.Collections.Generic;

namespace SLEAPI.Internal
{
  internal sealed class Run
  {
    public IList<PlayerMetadata> players { get; set; }
    public TimeMetadata times { get; set; }
  }
}