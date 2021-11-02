using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using Plants_Elements;

namespace Medical_plants_catalog
{
    public partial class Form1 : Form
    {
        PlantList pl;
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Shown(object sender, EventArgs e)
        {
            string path = Environment.CurrentDirectory + "\\plant_catalog.txt";
            pl = new PlantList(path);
            List<string> chemicalCompositionParams = new List<string>();
            for (int i = 0; i < pl.CountOfPlants; i++)
            {
                for (int j = 0; j < pl[i].chemicalComposition.Length; j++)
                {
                    if (!chemicalCompositionParams.Contains(pl[i].chemicalComposition[j]))
                    {
                        chemicalCompositionParams.Add(pl[i].chemicalComposition[j]);
                    }
                }
            }
            foreach(string s in chemicalCompositionParams)
            {
                checkedListBox_ChemicalComponents.Items.Add(s);
            }
            List<string> effectsParams = new List<string>();
            for (int i = 0; i < pl.CountOfPlants; i++)
            {
                for (int j = 0; j < pl[i].effect.Length; j++)
                {
                    if (!effectsParams.Contains(pl[i].effect[j]))
                    {
                        effectsParams.Add(pl[i].effect[j]);
                    }
                }
            }
            foreach (string s in effectsParams)
            {
                checkedListBox_Effects.Items.Add(s);
            }
            List<string> areaParams = new List<string>();
            for (int i = 0; i < pl.CountOfPlants; i++)
            {
                for (int j = 0; j < pl[i].area.Length; j++)
                {
                    if (!areaParams.Contains(pl[i].area[j]))
                    {
                        areaParams.Add(pl[i].area[j]);
                    }
                }
            }
            foreach (string s in areaParams)
            {
                checkedListBox_Areas.Items.Add(s);
            }
            for (int i = 0; i < pl.CountOfPlants; i++)
            {
                listBox_PlantList.Items.Add(pl[i].name);
            }
            listBox_PlantList.SelectedIndex = 0;
            richTextBox_PlantInformation.Text = pl.getInformationAboutPlant(listBox_PlantList.SelectedItem.ToString());
        }

        private void listBox_PlantList_SelectedValueChanged(object sender, EventArgs e)
        {
            richTextBox_PlantInformation.Text = pl.getInformationAboutPlant(listBox_PlantList.SelectedItem.ToString());
        }

        private void button_Search_Click(object sender, EventArgs e)
        {
            listBox_SearchResult.Items.Clear();
            List<string> requiredChemicalComposition = new List<string>();
            for (int i = 0; i < checkedListBox_ChemicalComponents.CheckedItems.Count; i++)
            {
                requiredChemicalComposition.Add(checkedListBox_ChemicalComponents.CheckedItems[i].ToString());
            }
            List<string> requiredEffects = new List<string>();
            for (int i = 0; i < checkedListBox_Effects.CheckedItems.Count; i++)
            {
                requiredEffects.Add(checkedListBox_Effects.CheckedItems[i].ToString());
            }
            List<string> requiredAreas = new List<string>();
            for (int i = 0; i < checkedListBox_Areas.CheckedItems.Count; i++)
            {
                requiredAreas.Add(checkedListBox_Areas.CheckedItems[i].ToString());
            }
            Request r = new Request(ref requiredChemicalComposition, ref requiredEffects, ref requiredAreas);
            List<string> requestResult = r.calculateRequest(ref pl);
            foreach (string s in requestResult)
            {
                listBox_SearchResult.Items.Add(s);
            }
        }

        private void listBox_SearchResult_SelectedValueChanged(object sender, EventArgs e)
        {
            richTextBox_PlantInformation.Text = pl.getInformationAboutPlant(listBox_SearchResult.SelectedItem.ToString());
        }
    }
}
