import os
import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


for k in range(2):
   if (k == 0):
      database_file = 'Twisted_2D_vdW_Bilayers_DFT_Optimization.json'
      POSCAR_files = 'POSCAR_Bilayers_DFT_Optimization'
   if (k == 1):
      database_file = 'Twisted_2D_vdW_Bilayers_All_Generated_Structures.json'
      POSCAR_files = 'POSCAR_Bilayers_All_Generated_Structures'
   #------------------------------------------------------------
   with open(database_file, "r") as file: data = json.load(file)
   df = pd.json_normalize(data if isinstance(data, list) else [data])
   tags = df.columns
   #-------------------------------------
   if os.path.isdir(POSCAR_files): 0 == 0
   else: os.mkdir(POSCAR_files)
   #---------------------------
   for material in data:
       #------------------------
       t_id = material.get("id")
       t_id_layers = material.get("id_layers")
       t_type_ions_layers = material.get("type_ions_layers")
       t_number_ions_layers = material.get("number_ions_layers")
       t_area_perc_mismatch = material.get("area_perc_mismatch")
       t_perc_area_change = material.get("perc_area_change")
       t_perc_mod_vectors_change = material.get("perc_mod_vectors_change")
       t_angle_perc_mismatch = material.get("angle_perc_mismatch")
       t_perc_angle_change = material.get("perc_angle_change")
       t_rotation_angle = material.get("rotation_angle")
       t_supercell_matrix = material.get("supercell_matrix")
       t_deformation_matrix = material.get("deformation_matrix")
       t_strain_matrix = material.get("strain_matrix")
       t_shift_plane = material.get("shift_plane")
       #--------------------------------------------------------
       vetor_A1 = material.get("a1")
       vetor_A2 = material.get("a2")
       vetor_A3 = material.get("a3") 
       type_ions = material.get("type_ions_layers") 
       type_nions = material.get("number_type_ions_layers")
       direct_coord = material.get("direct_coord_ions")
       #-----------------------------------------------
       label = "SAMBA"
       #--------------
       temp_str = ""
       for s in range(len(t_type_ions_layers)):
           if (s > 0): temp_str += "+"
           for t in range(len(t_type_ions_layers[s])): temp_str += str(t_type_ions_layers[s][t]) + "_"
           temp_str = temp_str[:-1]
       label += " " + temp_str
       #-----------
       for s in range(len(t_number_ions_layers)): label += " " + str(t_number_ions_layers[s])
       #----------------------------
       if (len(t_id_layers) > 1):
          #---------------------------------------------------
          label += " | mismatch_areas_12_21 = "; temp_str = ""
          for s in range(len(t_area_perc_mismatch)):
              for t in range(len(t_area_perc_mismatch[s])): temp_str += str(t_area_perc_mismatch[s][t]) + "_"
          temp_str = temp_str[:-1]
          label += temp_str
          #----------------------------------------
          label += " | var_areas = "; temp_str = ""
          for s in range(len(t_perc_area_change)): temp_str += str(t_perc_area_change[s]) + "_"
          temp_str = temp_str[:-1]
          label += temp_str
          #------------------------------------------
          label += " | var_vectors = "; temp_str = ""
          for s in range(len(t_perc_mod_vectors_change)):
              for t in range(len(t_perc_mod_vectors_change[s])): temp_str += str(t_perc_mod_vectors_change[s][t]) + "_"
          temp_str = temp_str[:-1]
          label += temp_str
          #----------------------------------------------------
          label += " | mismatch_angles_12_21 = "; temp_str = ""
          for s in range(len(t_angle_perc_mismatch)):
              for t in range(len(t_angle_perc_mismatch[s])): temp_str += str(t_angle_perc_mismatch[s][t]) + "_"
          temp_str = temp_str[:-1]
          label += temp_str
          #-----------------------------------------
          label += " | var_angles = "; temp_str = ""
          for s in range(len(t_perc_angle_change)): temp_str += str(t_perc_angle_change[s]) + "_"
          temp_str = temp_str[:-1]
          label += temp_str
          #---------------------------------------------------------
          label += " | rotation_angle = " + str(t_rotation_angle[0])
          #---------------------------------------
          for s in range(len(t_supercell_matrix)):
              if (s == 0): label += " | MSCell_1 = "; temp_str = ""
              if (s == 1): label += " | MSCell_2 = "; temp_str = ""
              if (s == 2): label += " | MSCell_3 = "; temp_str = ""
              for t in range(len(t_supercell_matrix[s])):
                  for r in range(len(t_supercell_matrix[s][t])):
                      temp_str += str(t_supercell_matrix[s][t][r]) + "_"
              temp_str = temp_str[:-1]
              label += temp_str
          #-----------------------------------------
          for s in range(len(t_deformation_matrix)):
              if (s == 0): label += " | MDeform_1 = "; temp_str = ""
              if (s == 1): label += " | MDeform_2 = "; temp_str = ""
              if (s == 2): label += " | MDeform_3 = "; temp_str = ""
              for t in range(len(t_deformation_matrix[s])):
                  for r in range(len(t_deformation_matrix[s][t])):
                      temp_str += str(t_deformation_matrix[s][t][r]) + "_"
              temp_str = temp_str[:-1]
              label += temp_str
          #------------------------------------
          for s in range(len(t_strain_matrix)):
              if (s == 0): label += " | MSTrain_1 = "; temp_str = ""
              if (s == 1): label += " | MSTrain_2 = "; temp_str = ""
              if (s == 2): label += " | MSTrain_3 = "; temp_str = ""
              for t in range(len(t_strain_matrix[s])):
                  for r in range(len(t_strain_matrix[s][t])):
                      temp_str += str(t_strain_matrix[s][t][r]) + "_"
              temp_str = temp_str[:-1]
              label += temp_str
          #------------------------
          if t_shift_plane is None:
             label += " | Shift_plane = 0.0_0.0 |"
          else:
             label += " | Shift_plane = "; temp_str = ""
             for s in range(len(t_shift_plane)): temp_str += str(t_shift_plane[s]) + "_"
             temp_str = temp_str[:-1] + " |"
             label += temp_str
          #-------------------------
          if (len(t_id_layers) > 1):
             for s in range(len(t_id_layers)):
                 if (len(t_id_layers) > 1): label += " " + str(t_id_layers[s])
       #---------------------------------------------
       label += " " + str(t_id)



       """
       SAMBA Si 2 Si2_70af89b1af9e43ed

       SAMBA In_Se+Fe_Ge_Te 5 6 | mismatch_areas_12_21 = -1.9354_1.9735 | var_areas = -0.97_0.9844 | var_vectors = -0.4862_-0.4862_0.491_0.491 | mismatch_angles_12_21 = 0.0_0.0 | var_angles = 0.0_0.0 | rotation_angle = 0.0 | MSCell_1 = -1_-1_-1_-1 | MSCell_2 = -1_-1_-1_-1 | MDeform_1 = 0.995137981_0.0_0.0_0.995137981 | MDeform_2 = 1.004909761_0.0_0.0_1.004909761 | MSTrain_1 = -0.004850199_0.0_0.0_-0.004850199 | MSTrain_2 = 0.004921814_0.0_0.0_0.004921814 | Shift_plane = 0.3333333333333333_0.3333333333333333 | In2Se3_6d22b0707c243278 Fe3GeTe2_511deec01ddee583 In2Se3+Fe3GeTe2_d5d210a98d396da6+b26dc340

       area_perc_mismatch: [ [-1.9354, 1.9735] ]
       perc_area_change: [-0.97, 0.9844]
       perc_mod_vectors_change: [ [-0.4862, -0.4862], [0.491, 0.491] ]
       angle_perc_mismatch: [ [0.0, 0.0] ]
       perc_angle_change: [0.0, 0.0]
       rotation_angle: [0.0]
       supercell_matrix: [ [[-1, -1], [-1, -1]], [[-1, -1], [-1, -1]] ]
       deformation_matrix: [ [[0.995137981, 0.0], [0.0, 0.995137981]], [[1.004909761, 0.0], [0.0, 1.004909761]] ]
       strain_matrix: [ [[-0.004850199, 0.0], [0.0, -0.004850199]], [[0.004921814, 0.0], [0.0, 0.004921814]] ]
       shift_plane: [0.333333333333333, 0.333333333333333]
       """



       #-----------------------------------------------------------
       poscar = open(POSCAR_files + '/' + str(t_id) + '.vasp', "w")
       poscar.write(f'{label} \n')
       poscar.write(f'1.0 \n')
       poscar.write(f'{vetor_A1[0]} {vetor_A1[1]} {vetor_A1[2]} \n')
       poscar.write(f'{vetor_A2[0]} {vetor_A2[1]} {vetor_A2[2]} \n')
       poscar.write(f'{vetor_A3[0]} {vetor_A3[1]} {vetor_A3[2]} \n')
       #------------------------------
       for i in range(len(type_ions)):
           for j in range(len(type_ions[i])):
               poscar.write(f'{type_ions[i][j]} ')
       poscar.write(f' \n')
       #-------------------------------
       for i in range(len(type_nions)):
           for j in range(len(type_nions[i])):
               poscar.write(f'{type_nions[i][j]} ')
       poscar.write(f' \n')
       #-------------------------
       poscar.write(f'Direct \n')
       #---------------------------------
       for i in range(len(direct_coord)): poscar.write(f'{direct_coord[i][0]} {direct_coord[i][1]} {direct_coord[i][2]} \n')
       #---------------------------------
       poscar.close()
       #-------------

print(" ")
print("===============================")
print("Extracted POSCAR files: =======")
print("===============================")



