import os
import re



def main():
    making_maintf()
    making_outputstf()
    making_variablestf()



def get_namelist(prefix, postfix, file_path):
    array = []
    file = open(file_path)
    for line in file:
        result = re.match("^" + prefix + "[A-z]*" + postfix + "$", line)
        if result:
            result_str = "{}".format(result.group(0))
            result_str = result_str[len(prefix):len(result_str)-len(postfix)]
            array.append(result_str)
    return array



def text_addition(file_path, test_postfix):
    file = open(file_path, "a")
    file.write(test_postfix)
    file.close()



def spaces_generator(count):
    spases = ""
    for i in range(count):
        spases = spases + " "
    return spases



def making_variablestf():
    file = open("../variables.tf")
    text_addition("examples/variables.tf", "\n")
    for line in file:
        text_addition("examples/variables.tf", line)



def making_outputstf():
    outputs_list = get_namelist("output \"", "\" {", "../outputs.tf")
    for __index__ in range(len(outputs_list)):
        output_string = "\noutput \"" + outputs_list[__index__] + "\" {\n  value = \"${module." + "{{ cookiecutter.example_module_name}}" + "." + outputs_list[__index__] + "}\"\n}\n"
        text_addition("examples/outputs.tf", output_string)



def making_maintf():
    variables_list = get_namelist("variable \"", "\" {", "../variables.tf")
    text_addition("examples/main.tf", "\nmodule \"" + "{{ cookiecutter.example_module_name}}" + "\" {\n")

    bigest_len = 0
    for __index__ in range(len(variables_list)):
        if bigest_len < len(variables_list[__index__]):
            bigest_len = len(variables_list[__index__])

    for __index__ in range(len(variables_list)):
        variable_string = "  " + variables_list[__index__] + spaces_generator(bigest_len - len(variables_list[__index__])) + " = \"${var." + variables_list[__index__] + "}\"\n"
        text_addition("examples/main.tf", variable_string)
    text_addition("examples/main.tf", "  source" + spaces_generator(bigest_len - len("source")) + " = \"../../\"\n}\n")




if __name__== "__main__":
    main()
    os.remove("../terratest")
