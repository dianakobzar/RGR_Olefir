namespace Medical_plants_catalog
{
    partial class Form1
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.openFileDialog_PlantsInfoLoader = new System.Windows.Forms.OpenFileDialog();
            this.listBox_PlantList = new System.Windows.Forms.ListBox();
            this.label1 = new System.Windows.Forms.Label();
            this.label2 = new System.Windows.Forms.Label();
            this.richTextBox_PlantInformation = new System.Windows.Forms.RichTextBox();
            this.listBox_SearchResult = new System.Windows.Forms.ListBox();
            this.label3 = new System.Windows.Forms.Label();
            this.checkedListBox_ChemicalComponents = new System.Windows.Forms.CheckedListBox();
            this.checkedListBox_Effects = new System.Windows.Forms.CheckedListBox();
            this.checkedListBox_Areas = new System.Windows.Forms.CheckedListBox();
            this.label4 = new System.Windows.Forms.Label();
            this.label5 = new System.Windows.Forms.Label();
            this.label6 = new System.Windows.Forms.Label();
            this.button_Search = new System.Windows.Forms.Button();
            this.SuspendLayout();
            // 
            // listBox_PlantList
            // 
            this.listBox_PlantList.Font = new System.Drawing.Font("Microsoft Sans Serif", 11.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.listBox_PlantList.FormattingEnabled = true;
            this.listBox_PlantList.ItemHeight = 18;
            this.listBox_PlantList.Location = new System.Drawing.Point(12, 32);
            this.listBox_PlantList.Name = "listBox_PlantList";
            this.listBox_PlantList.Size = new System.Drawing.Size(243, 238);
            this.listBox_PlantList.TabIndex = 0;
            this.listBox_PlantList.SelectedValueChanged += new System.EventHandler(this.listBox_PlantList_SelectedValueChanged);
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Font = new System.Drawing.Font("Microsoft Sans Serif", 11.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.label1.Location = new System.Drawing.Point(12, 9);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(118, 18);
            this.label1.TabIndex = 1;
            this.label1.Text = "Список рослин:";
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Font = new System.Drawing.Font("Microsoft Sans Serif", 11.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.label2.Location = new System.Drawing.Point(610, 15);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(241, 18);
            this.label2.TabIndex = 2;
            this.label2.Text = "Інформація про вибрану рослину:";
            // 
            // richTextBox_PlantInformation
            // 
            this.richTextBox_PlantInformation.Font = new System.Drawing.Font("Microsoft Sans Serif", 11.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.richTextBox_PlantInformation.Location = new System.Drawing.Point(613, 32);
            this.richTextBox_PlantInformation.Name = "richTextBox_PlantInformation";
            this.richTextBox_PlantInformation.Size = new System.Drawing.Size(359, 667);
            this.richTextBox_PlantInformation.TabIndex = 3;
            this.richTextBox_PlantInformation.Text = "";
            // 
            // listBox_SearchResult
            // 
            this.listBox_SearchResult.Font = new System.Drawing.Font("Microsoft Sans Serif", 11.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.listBox_SearchResult.FormattingEnabled = true;
            this.listBox_SearchResult.ItemHeight = 18;
            this.listBox_SearchResult.Location = new System.Drawing.Point(12, 374);
            this.listBox_SearchResult.Name = "listBox_SearchResult";
            this.listBox_SearchResult.Size = new System.Drawing.Size(243, 310);
            this.listBox_SearchResult.TabIndex = 4;
            this.listBox_SearchResult.SelectedValueChanged += new System.EventHandler(this.listBox_SearchResult_SelectedValueChanged);
            // 
            // label3
            // 
            this.label3.AutoSize = true;
            this.label3.Font = new System.Drawing.Font("Microsoft Sans Serif", 11.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.label3.Location = new System.Drawing.Point(12, 355);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(146, 18);
            this.label3.TabIndex = 9;
            this.label3.Text = "Результати пошуку:";
            // 
            // checkedListBox_ChemicalComponents
            // 
            this.checkedListBox_ChemicalComponents.Font = new System.Drawing.Font("Microsoft Sans Serif", 11.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.checkedListBox_ChemicalComponents.FormattingEnabled = true;
            this.checkedListBox_ChemicalComponents.Location = new System.Drawing.Point(286, 32);
            this.checkedListBox_ChemicalComponents.Name = "checkedListBox_ChemicalComponents";
            this.checkedListBox_ChemicalComponents.Size = new System.Drawing.Size(289, 194);
            this.checkedListBox_ChemicalComponents.TabIndex = 11;
            // 
            // checkedListBox_Effects
            // 
            this.checkedListBox_Effects.Font = new System.Drawing.Font("Microsoft Sans Serif", 11.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.checkedListBox_Effects.FormattingEnabled = true;
            this.checkedListBox_Effects.Location = new System.Drawing.Point(286, 274);
            this.checkedListBox_Effects.Name = "checkedListBox_Effects";
            this.checkedListBox_Effects.Size = new System.Drawing.Size(289, 194);
            this.checkedListBox_Effects.TabIndex = 12;
            // 
            // checkedListBox_Areas
            // 
            this.checkedListBox_Areas.Font = new System.Drawing.Font("Microsoft Sans Serif", 11.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.checkedListBox_Areas.FormattingEnabled = true;
            this.checkedListBox_Areas.Location = new System.Drawing.Point(286, 509);
            this.checkedListBox_Areas.Name = "checkedListBox_Areas";
            this.checkedListBox_Areas.Size = new System.Drawing.Size(295, 175);
            this.checkedListBox_Areas.TabIndex = 13;
            // 
            // label4
            // 
            this.label4.AutoSize = true;
            this.label4.Font = new System.Drawing.Font("Microsoft Sans Serif", 11.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.label4.Location = new System.Drawing.Point(286, 9);
            this.label4.Name = "label4";
            this.label4.Size = new System.Drawing.Size(142, 18);
            this.label4.TabIndex = 14;
            this.label4.Text = "Хімічні компоненти";
            // 
            // label5
            // 
            this.label5.AutoSize = true;
            this.label5.Font = new System.Drawing.Font("Microsoft Sans Serif", 11.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.label5.Location = new System.Drawing.Point(286, 253);
            this.label5.Name = "label5";
            this.label5.Size = new System.Drawing.Size(100, 18);
            this.label5.TabIndex = 15;
            this.label5.Text = "Лікувальні дії";
            // 
            // label6
            // 
            this.label6.AutoSize = true;
            this.label6.Font = new System.Drawing.Font("Microsoft Sans Serif", 11.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.label6.Location = new System.Drawing.Point(283, 488);
            this.label6.Name = "label6";
            this.label6.Size = new System.Drawing.Size(222, 18);
            this.label6.TabIndex = 16;
            this.label6.Text = "Область поширення по Україні";
            // 
            // button_Search
            // 
            this.button_Search.Font = new System.Drawing.Font("Microsoft Sans Serif", 11.25F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.button_Search.Location = new System.Drawing.Point(12, 288);
            this.button_Search.Name = "button_Search";
            this.button_Search.Size = new System.Drawing.Size(243, 59);
            this.button_Search.TabIndex = 17;
            this.button_Search.Text = "Шукати рослини за обраними параметрами";
            this.button_Search.UseVisualStyleBackColor = true;
            this.button_Search.Click += new System.EventHandler(this.button_Search_Click);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(984, 711);
            this.Controls.Add(this.button_Search);
            this.Controls.Add(this.label6);
            this.Controls.Add(this.label5);
            this.Controls.Add(this.label4);
            this.Controls.Add(this.checkedListBox_Areas);
            this.Controls.Add(this.checkedListBox_Effects);
            this.Controls.Add(this.checkedListBox_ChemicalComponents);
            this.Controls.Add(this.label3);
            this.Controls.Add(this.listBox_SearchResult);
            this.Controls.Add(this.richTextBox_PlantInformation);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.listBox_PlantList);
            this.FormBorderStyle = System.Windows.Forms.FormBorderStyle.FixedDialog;
            this.Name = "Form1";
            this.Text = "Довідник лікарських рослин (виконав Пилипченко Богдан)";
            this.Shown += new System.EventHandler(this.Form1_Shown);
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion
        private System.Windows.Forms.OpenFileDialog openFileDialog_PlantsInfoLoader;
        private System.Windows.Forms.ListBox listBox_PlantList;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.RichTextBox richTextBox_PlantInformation;
        private System.Windows.Forms.ListBox listBox_SearchResult;
        private System.Windows.Forms.Label label3;
        private System.Windows.Forms.CheckedListBox checkedListBox_ChemicalComponents;
        private System.Windows.Forms.CheckedListBox checkedListBox_Effects;
        private System.Windows.Forms.CheckedListBox checkedListBox_Areas;
        private System.Windows.Forms.Label label4;
        private System.Windows.Forms.Label label5;
        private System.Windows.Forms.Label label6;
        private System.Windows.Forms.Button button_Search;
    }
}

