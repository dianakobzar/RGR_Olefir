using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Plants_Elements;

namespace Plants_Elements
{
    class Request
    {
        private string[] chemicalComposition;
        private string[] effect;
        private string[] area;

        public Request(ref List<string> O_chemicalComposition, ref List<string> O_effect, ref List<string> O_area)
        {
            chemicalComposition = new string[O_chemicalComposition.Count];
            O_chemicalComposition.CopyTo(chemicalComposition, 0);
            effect = new string[O_effect.Count];
            O_effect.CopyTo(effect, 0);
            area = new string[O_area.Count];
            O_area.CopyTo(area, 0);
        }

        public List<string> calculateRequest(ref PlantList pl)
        {
            List<string> result = new List<string>();
            for (int i = 0; i < pl.CountOfPlants; i++)
            {
                if (checkPlantForRequest(pl[i]))
                {
                    result.Add(pl[i].name);
                }
            }
            return result;
        }

        private bool checkPlantForRequest(Plant p)
        {
            return (checkForChemicalComposition(p) && checkForEffect(p) && checkForArea(p));
        }

        private bool checkForChemicalComposition(Plant p)
        {
            return Enumerable.SequenceEqual(chemicalComposition.Intersect(p.chemicalComposition), chemicalComposition);
        }

        private bool checkForEffect(Plant p)
        {
            return Enumerable.SequenceEqual(effect.Intersect(p.effect), effect);
        }

        private bool checkForArea(Plant p)
        {
            return Enumerable.SequenceEqual(area.Intersect(p.area), area);
        }
    }
}
