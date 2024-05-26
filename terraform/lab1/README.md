# Terraform useful commands

## Init Terraform
```
terraform init
```

## Apply Terraform configuration script
```
terraform apply
```

## Inspecting Infrastructure

### Generate Dependencies Graph

The terraform graph command produces descriptions of the relationships between objects in a Terraform configuration, using the DOT language.

```
terraform graph -type=plan | dot -Tpng >graph.png
```

### List Infrastructure

The terraform state list command is used to list resources within a Terraform state.

```
terraform state list
```

### Show Infrastructure

The terraform show command is used to provide human-readable output from a state or plan file. This can be used to inspect a plan to ensure that the planned operations are expected, or to inspect the current state as Terraform sees it.

```
terraform show
```

### Show Resource State

The terraform state show command is used to show the attributes of a single resource in the Terraform state.

```
terraform state show 'google_compute_instance.epimenides'
```

### Export config
Export the generated config to a file called generated.tf
terraform plan -generate-config-out=generated.tf