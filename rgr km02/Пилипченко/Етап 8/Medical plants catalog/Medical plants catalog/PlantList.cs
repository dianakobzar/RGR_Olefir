using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.IO;

namespace Plants_Elements
{
    class PlantList
    {
        private List<Plant> plants;
        public int CountOfPlants
        {
            get
            {
                return plants.Count;
            }
        }
        public Plant this[int i]
        {
            get
            {
                return plants[i];
            }
        }

        public PlantList(string path)
        {
            StreamReader sr = new StreamReader(path);
            plants = new List<Plant>();
            int temp = Convert.ToInt32(sr.ReadLine());
            for (int i = 0; i < temp; i++)
            {
                string nameOfCurrentPlant = sr.ReadLine();
                string descriptionOfCurrentPlant = sr.ReadLine();
                string[] chemicalCompositionOfCurrentPlant = sr.ReadLine().Split(',');
                string[] effectsOfCurrentPlant = sr.ReadLine().Split(',');
                string[] areaOfCurrentPlant = sr.ReadLine().Split(',');
                plants.Add(new Plant(nameOfCurrentPlant, descriptionOfCurrentPlant, ref chemicalCompositionOfCurrentPlant, ref effectsOfCurrentPlant, ref areaOfCurrentPlant));
            }
            sr.Close();
        }

        public Plant getPlantByName(string searchedName)
        {
            foreach (Plant currentPlant in plants)
            {
                if (currentPlant.name == searchedName)
                {
                    return currentPlant;
                }
            }
            return null;
        }

        public string getInformationAboutPlant(string plantName)
        {
            Plant p = getPlantByName(plantName);
            string result = "Назва: " + p.name + Environment.NewLine + Environment.NewLine + "Опис:" + Environment.NewLine + p.description + Environment.NewLine + Environment.NewLine + "Хімічний склад:" + Environment.NewLine;
            foreach (string currentComponent in p.chemicalComposition)
            {
                result += currentComponent + "; ";
            }
            result += Environment.NewLine + Environment.NewLine + "Лікувальні дії:" + Environment.NewLine;
            foreach (string currentEffect in p.effect)
            {
                result += currentEffect + "; ";
            }
            result += Environment.NewLine + Environment.NewLine + "Область поширення на території України:" + Environment.NewLine;
            foreach (string currentArea in p.area)
            {
                result += currentArea + "; ";
            }
            return result;
        }
    }
}
