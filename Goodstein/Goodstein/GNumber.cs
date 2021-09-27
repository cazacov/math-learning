using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Numerics;
using System.Text;

namespace Goodstein
{
    [DebuggerDisplay("{" + nameof(val) + "}")]
    public class GNumber
    {
        private long Last;
        private Dictionary<GNumber, long> Nodes = new Dictionary<GNumber, long>();
        private BigInteger val;
        private BigInteger baseValue;
        
        public static GNumber Create(long number, long b)
        {
            var result = new GNumber();

            result.val = number;
            result.Last = number % b;
            number /= b;

            long power = 0;
            while (number > 0)
            {
                var rest = number % b;
                number /= b;
                power++;
                if (rest > 0)
                {
                    var p = GNumber.Create(power, b);
                    result.Nodes[p] = rest;
                }
            }
            return result;
        }

        protected bool Equals(GNumber other)
        {
            return Last == other.Last && Equals(Nodes, other.Nodes);
        }

        public override bool Equals(object obj)
        {
            if (ReferenceEquals(null, obj)) return false;
            if (ReferenceEquals(this, obj)) return true;
            if (obj.GetType() != this.GetType()) return false;
            return Equals((GNumber) obj);
        }

        public override int GetHashCode()
        {
            return HashCode.Combine(Last, Nodes);
        }
    }
}
