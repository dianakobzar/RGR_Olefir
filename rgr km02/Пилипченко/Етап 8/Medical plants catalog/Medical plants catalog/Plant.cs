using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.IO;

namespace Plants_Elements
{
    class Plant
    {
        public string name;
        public string description;
        public string[] chemicalComposition;
        public string[] effect;
        public string[] area;

        public Plant(string O_name, string O_description, ref string[] O_chemicalComposition, ref string[] O_effect, ref string[] O_area)
        {
            name = O_name;
            description = O_description;
            area = new string[O_area.Length];
            O_area.CopyTo(area, 0);
            chemicalComposition = new string[O_chemicalComposition.Length];
            O_chemicalComposition.CopyTo(chemicalComposition, 0);
            effect = new string[O_effect.Length];
            O_effect.CopyTo(effect, 0);
        }
    }
        
}
