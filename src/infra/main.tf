provider "azurerm" {
  features {}
}

resource "azurerm_resource_group" "sama_rg" {
  name     = "sama-resilience-rg"
  location = "Saudi Arabia Central"
}

resource "azurerm_kubernetes_cluster" "sama_aks" {
  name                = "sama-aks"
  location            = azurerm_resource_group.sama_rg.location
  resource_group_name = azurerm_resource_group.sama_rg.name
  dns_prefix          = "sama-aks"

  default_node_pool {
    name       = "system"
    node_count = 2
    vm_size    = "Standard_DS2_v2"
  }

  identity {
    type = "SystemAssigned"
  }
}
