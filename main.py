import os
import zipfile
import shutil
import xml.etree.ElementTree as ET

def modify_metadata(file_path, new_version):
    """Modify the version in metadata.txt"""
    with open(file_path, 'r') as file:
        lines = file.readlines()

    with open(file_path, 'w') as file:
        for line in lines:
            if line.startswith("version="):
                file.write(f"version={new_version}\n")
            else:
                file.write(line)

def zip_project_folder(folder_path, output_zip):
    """Zip the entire project folder"""
    with zipfile.ZipFile(output_zip, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, folder_path)
                zipf.write(file_path, arcname)



def modify_xml(file_path, release_version):
    """Modify the version attribute in the pyqgis_plugin XML element."""

    with open(file_path, "r", encoding="utf-8") as file:
        lines = file.readlines()

    if lines[0].strip().startswith("<?xml"):
        lines[0] = f"<?xml version='{release_version}' encoding='utf-8'?>\n"
    if lines[2].strip().startswith("<pyqgis_plugin"):
            lines[2] = f'<pyqgis_plugin name="Booster" version="{release_version}">\n'
    print(lines)
    with open(file_path, "w", encoding="utf-8") as file:
        file.writelines(lines)


    #tree = ET.parse(file_path)
    #root = tree.getroot()


    #root[0].set("version",release_version)

    #tree.write(file_path, encoding="utf-8", xml_declaration=True)

if __name__ == "__main__":
    # Paths to files and folders
    project_folder = "/Users/Wattmen/Library/Application Support/QGIS/QGIS3/profiles/default/python/plugins/Booster"  # Change to your project folder path
    metadata_file = os.path.join(project_folder, "metadata.txt")
    xml_file = "./plugins.xml"
    zip_output = "./booster_release/Booster.zip"


    # Version details
    new_version = "0.4"
    release_version = new_version#"1.0.0"

    # Step 1: Modify metadata.txt
    modify_metadata(metadata_file, new_version)
    print(f"Updated metadata.txt with version {new_version}.")

    # Step 2: Zip the project folder
    #zip_project_folder(project_folder, zip_output)
    #print(f"Project folder zipped to {zip_output}.")

    # Step 3: Modify the XML file
    modify_xml(xml_file, release_version)
    print(f"Updated XML file {xml_file} with release version {release_version}.")
