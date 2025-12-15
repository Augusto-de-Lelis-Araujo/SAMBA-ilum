import os
import sys
import json
import pandas as pd

def atoms_folder(natoms):
    if 2 <= natoms <= 10:   return "2-10atoms"
    if 11 <= natoms <= 20:  return "11-20atoms"
    if 21 <= natoms <= 30:  return "21-30atoms"
    if 31 <= natoms <= 40:  return "31-40atoms"
    if 41 <= natoms <= 50:  return "41-50atoms"
    if 51 <= natoms <= 60:  return "51-60atoms"
    if 61 <= natoms <= 70:  return "61-70atoms"
    if 71 <= natoms <= 80:  return "71-80atoms"
    if 81 <= natoms <= 90:  return "81-90atoms"
    if 91 <= natoms <= 100: return "91-100atoms"
    return "out_of_range"

for k in range(2):
    if (k == 0):
        database_file = 'json_files/Twisted_2D_vdW_All_DFT_Calculations.json'
        POSCAR_files = 'POSCAR_Bilayers_DFT_Optimization'
    if (k == 1):
        database_file = 'json_files/Twisted_2D_vdW_Bilayers_All_Generated_Structures.json'
        POSCAR_files = 'POSCAR_Bilayers_All_Generated_Structures'
    
    #------------------------------------------------------------
    if not os.path.exists(database_file):
        print(f"Aviso: Arquivo {database_file} não encontrado. Pulando...")
        continue

    with open(database_file, "r", encoding='utf-8') as file: 
        data = json.load(file)
    
    #----------------
    if (k == 0):
        print("\n" + f'Extracting POSCAR files from All DFT Calculations: {len(data)}')
    if (k == 1):
        print("\n" + f'Extracting POSCAR files from All Generated Bilayers: {len(data)}')
    
    #--------------------------------------------
    temp = 1.0; number = -1; n_passos = len(data)
    
    for material in data:
        number += 1
        porc = (number/n_passos)*100        
        
        if porc >= temp:
            bar_length = 50
            filled_length = int(bar_length * porc // 100)
            bar = '#' * filled_length + '-' * (bar_length - filled_length)
            print(f'\rProgress: |{bar}| {porc:.1f}%', end="")
            sys.stdout.flush()
            temp += 1
        
        # Extração de dados
        t_id = material.get("id")
        t_id_layers = material.get("id_layers")
        t_nions = material.get("number_ions")
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
        
        vetor_A1 = material.get("a1")
        vetor_A2 = material.get("a2")
        vetor_A3 = material.get("a3") 
        type_ions = material.get("type_ions_layers") 
        type_nions = material.get("number_type_ions_layers")
        direct_coord = material.get("direct_coord_ions")

        # Construção da Label
        label = "SAMBA"
        temp_str = ""
        for s in range(len(t_type_ions_layers)):
            if (s > 0): temp_str += "+"
            for t in range(len(t_type_ions_layers[s])): temp_str += str(t_type_ions_layers[s][t]) + "_"
            temp_str = temp_str[:-1]
        label += " " + temp_str
        
        for s in range(len(t_number_ions_layers)): label += " " + str(t_number_ions_layers[s])
        
        if (len(t_id_layers) > 1):
            label += " | mismatch_areas_12_21 = "; temp_str = ""
            for s in range(len(t_area_perc_mismatch)):
                for t in range(len(t_area_perc_mismatch[s])): temp_str += str(t_area_perc_mismatch[s][t]) + "_"
            temp_str = temp_str[:-1]; label += temp_str

            label += " | var_areas = "; temp_str = ""
            for s in range(len(t_perc_area_change)): temp_str += str(t_perc_area_change[s]) + "_"
            temp_str = temp_str[:-1]; label += temp_str

            label += " | var_vectors = "; temp_str = ""
            for s in range(len(t_perc_mod_vectors_change)):
                for t in range(len(t_perc_mod_vectors_change[s])): temp_str += str(t_perc_mod_vectors_change[s][t]) + "_"
            temp_str = temp_str[:-1]; label += temp_str

            label += " | mismatch_angles_12_21 = "; temp_str = ""
            for s in range(len(t_angle_perc_mismatch)):
                for t in range(len(t_angle_perc_mismatch[s])): temp_str += str(t_angle_perc_mismatch[s][t]) + "_"
            temp_str = temp_str[:-1]; label += temp_str

            label += " | var_angles = "; temp_str = ""
            for s in range(len(t_perc_angle_change)): temp_str += str(t_perc_angle_change[s]) + "_"
            temp_str = temp_str[:-1]; label += temp_str

            label += " | rotation_angle = " + str(t_rotation_angle[0])

            for s in range(len(t_supercell_matrix)):
                if (s == 0): label += " | MSCell_1 = "
                if (s == 1): label += " | MSCell_2 = "
                if (s == 2): label += " | MSCell_3 = "
                temp_str = ""
                for t in range(len(t_supercell_matrix[s])):
                    for r in range(len(t_supercell_matrix[s][t])):
                        temp_str += str(t_supercell_matrix[s][t][r]) + "_"
                label += temp_str[:-1]

            for s in range(len(t_deformation_matrix)):
                if (s == 0): label += " | MDeform_1 = "
                if (s == 1): label += " | MDeform_2 = "
                if (s == 2): label += " | MDeform_3 = "
                temp_str = ""
                for t in range(len(t_deformation_matrix[s])):
                    for r in range(len(t_deformation_matrix[s][t])):
                        temp_str += str(t_deformation_matrix[s][t][r]) + "_"
                label += temp_str[:-1]

            for s in range(len(t_strain_matrix)):
                if (s == 0): label += " | MSTrain_1 = "
                if (s == 1): label += " | MSTrain_2 = "
                if (s == 2): label += " | MSTrain_3 = "
                temp_str = ""
                for t in range(len(t_strain_matrix[s])):
                    for r in range(len(t_strain_matrix[s][t])):
                        temp_str += str(t_strain_matrix[s][t][r]) + "_"
                label += temp_str[:-1]

            if t_shift_plane is None:
                label += " | Shift_plane = 0.0_0.0 |"
            else:
                label += " | Shift_plane = "; temp_str = ""
                for s in range(len(t_shift_plane)): temp_str += str(t_shift_plane[s]) + "_"
                label += temp_str[:-1] + " |"

            for s in range(len(t_id_layers)): label += " " + str(t_id_layers[s])

        label += " " + str(t_id)

        # Lógica de Diretórios
        folder_atoms = atoms_folder(t_nions)
        output_dir = os.path.join(POSCAR_files, folder_atoms)

        # Nome do arquivo
        if (len(t_id_layers) == 1):
            filename = f"{t_nions}atoms_{t_id}.vasp"
        else:
            filename = f"{t_nions}atoms_{t_rotation_angle[0]}º_{t_id}.vasp"

        # CORREÇÃO: Cria a pasta e todas as subpastas necessárias no caminho
        # O parâmetro exist_ok=True evita o erro se a pasta já existir.
        if not os.path.exists(output_dir):
            os.makedirs(output_dir, exist_ok=True)

        # Escrita do arquivo
        try:
            with open(os.path.join(output_dir, filename), "w", encoding='utf-8') as poscar:
                poscar.write(f'{label} \n')
                poscar.write(f'1.0 \n')
                poscar.write(f'{vetor_A1[0]} {vetor_A1[1]} {vetor_A1[2]} \n')
                poscar.write(f'{vetor_A2[0]} {vetor_A2[1]} {vetor_A2[2]} \n')
                poscar.write(f'{vetor_A3[0]} {vetor_A3[1]} {vetor_A3[2]} \n')
                
                for i in range(len(type_ions)):
                    for j in range(len(type_ions[i])):
                        poscar.write(f'{type_ions[i][j]} ')
                poscar.write(f' \n')
                
                for i in range(len(type_nions)):
                    for j in range(len(type_nions[i])):
                        poscar.write(f'{type_nions[i][j]} ')
                poscar.write(f' \n')
                
                poscar.write(f'Direct \n')
                for i in range(len(direct_coord)): 
                    poscar.write(f'{direct_coord[i][0]} {direct_coord[i][1]} {direct_coord[i][2]} \n')
        except Exception as e:
            print(f"\nErro ao salvar o arquivo {filename}: {e}")

    print(f"\rProgress completed !{' ' * 60}")

print("\n===============================")
print("Extracted POSCAR files: =======")
print("===============================")