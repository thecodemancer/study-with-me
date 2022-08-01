# Terraform 101

## Overview

Terraform enables you to safely and predictably create, change, and improve infrastructure. It is an open-source tool that codifies APIs into declarative configuration files that can be shared among team members, treated as code, edited, reviewed, and versioned.

In this lab, you create a Terraform configuration with a module to automate the deployment of Google Cloud infrastructure. Specifically, you deploy one auto mode network with a firewall rule and two VM instances, as shown in this diagram:

![](images/terraform_diagram.png)

## Objectives

In this lab, you learn how to perform the following tasks:

* Create a configuration for an auto mode network
* Create a configuration for a firewall rule
* Create a module for VM instances
* Create and deploy a configuration
* Verify the deployment of a configuration

## Task 1. Set up Terraform and Cloud Shell

1. In the Cloud Console, click **Activate Cloud Shell** (Activate Cloud Shell icon).

2. If prompted, click **Continue**.

3. To confirm that Terraform is installed, run the following command:

`terraform --version`

## Task 2. Create mynetwork and its resources

Create the following file structure:

* instance
   * main.tf
   * variables.tf
* mynetwork.tf
* provider.tf

Then, paste the code provided in this repo. After that, follow these instructions to apply the mynetwork configuration.

1. To rewrite the Terraform configuration files to a canonical format and style, run the following command:

`terraform fmt`

2. To initialize Terraform, run the following command:

`terraform init`

3. To create an execution plan, run the following command:

`terraform plan`

Terraform determined that the following 4 resources need to be added:

| Name      | Description |
| ----------- | ----------- |
| mynetwork      | VPC network       |
| mynetwork-allow-http-ssh-rdp-icmp   | Firewall rule to allow HTTP, SSH, RDP and ICMP        |
| mynet-us-vm   | VM instance in us-central1-a       |
| mynet-eu-vm   | VM instance in europe-west1-d      |
	
4. To apply the desired changes, run the following command:

`terraform apply`

5. To confirm the planned actions, type:

`yes`

## Task 3. Verify your deployment

### Verify your network in the Cloud Console

1. In the Cloud Console, on the **Navigation menu**, click **VPC network** > **VPC networks**.

2. View the **mynetwork** VPC network with a subnetwork in every region.

3. On the **Navigation menu**, click **VPC network** > **Firewall**.

4. Sort the firewall rules by **Network**.

5. View the **mynetwork-allow-http-ssh-rdp-icmp** firewall rule for **mynetwork**.

### Verify your VM instances in the Cloud Console

1. On the **Navigation menu**, click **Compute Engine** > **VM instances**.

2. View the **mynet-us-vm** and **mynet-eu-vm** instances.

3. Note the internal IP address for **mynet-eu-vm**.

4. For **mynet-us-vm**, click **SSH** to launch a terminal and connect.

5. To test connectivity to **mynet-eu-vm**'s internal IP address, run the following command in the SSH terminal (replacing mynet-eu-vm's internal IP address with the value noted earlier):

`ping -c 3 <Enter mynet-eu-vm's internal IP here>`

## Task 4. Review

In this lab, you created a Terraform configuration with a module to automate the deployment of Google Cloud infrastructure. As your configuration changes, Terraform can create incremental execution plans, which allows you to build your overall configuration step by step.

The instance module allowed you to re-use the same resource configuration for multiple resources while providing properties as input variables. You can leverage the configuration and module that you created as a starting point for future deployments.
