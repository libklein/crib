"""
Crib application
"""
from crib import injection
from crib.config import LoadedConfiguration
from crib.plugin_loader import ConfiguredPluginProvider, PluginsProvider, hook
from crib.services.properties import PropertyService


class AppContainer(injection.Container):
    config_file = None
    config = injection.SingletonProvider(LoadedConfiguration)
    config_loaders = PluginsProvider(hook.crib_add_config_loaders)
    directions_service = ConfiguredPluginProvider(hook.crib_add_directions_services)
    directions_repository = ConfiguredPluginProvider(hook.crib_add_directions_repos)
    user_repository = ConfiguredPluginProvider(hook.crib_add_user_repos)
    property_service = injection.SingletonProvider(PropertyService)
    property_repository = ConfiguredPluginProvider(hook.crib_add_property_repos)
