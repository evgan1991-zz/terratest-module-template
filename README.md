# Terratest module template

## Description
This tool is designed to automatically generate a simple test pattern for [Terraform](https://www.terraform.io/) modules using [Terratest](https://github.com/gruntwork-io/terratest). Tool automatically creates additional folders and adds the files necessary for the tests. The only test added by this script checks the possibility to create and destroy a resource created by your terraform module.


## How to use:
```hcl
pip install cookiecutter
```
... and go to your module root-folder.

For creating test:
```hcl
cookiecutter https://github.com/evgan1991/terratest-module-template --no-input
```

For running test:
go to folder 'terratest/test'
```hcl
go test
```

## Files to be added
 * examples/main.tf
 * examples/variables.tf
 * examples/outputs.tf
 * [test/tf_module_test.go]


## [tf_module_test.go]({{ cookiecutter.terratest_folder_name }}/test/tf_module_test.go)
In order to avoid a name conflict during execution, a random line of text is added to the name of the resource. By default, the name is set by the parameter "name" in the description of the structure that is passed to the module as input parameters.
```hcl
Vars: map[string]interface{}{
    "aws_region": region,
    "name"      : "test_name_" + randSeq(10),
},
```
If the variable name or any other identifier of your resource has a different name, change this name in [tf_module_test.go]({{ cookiecutter.terratest_folder_name }}/test/tf_module_test.go)
If your module has require variables, tool shows to you list with these variables. WARNING! Add these variables to [tf_module_test.go]({{ cookiecutter.terratest_folder_name }}/test/tf_module_test.go)


## Tests
You can see results of test by this [link](https://sonarcloud.io/dashboard?id=evgan1991_terratest-module-template).


## Terraform versions
Terraform v0.11.13


## GO versions
go version go1.12 darwin/amd64


## Python version
Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 29 2018)


## License

Apache


## Authors

authors:
  - Yauheni Anashkin
