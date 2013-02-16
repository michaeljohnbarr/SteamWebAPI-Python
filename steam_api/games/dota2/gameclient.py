class IGCVersion_570(SteamWebAPI):
    def __init__(self):
        self.interface = 'IGCVersion_570'
        super(IGCVersion_570, self).__init__()

    def GetClientVersion(self):
        params = {}
        return self.generate_api_url(self.interface, 'GetClientVersion', 1,
            params, key=True)

    def GetClusterVersion(self):
        params = {}
        return self.generate_api_url(self.interface, 'GetClusterVersion', 1,
            params, key=True)

    def GetServerVersion(self):
        params = {}
        return self.generate_api_url(self.interface, 'GetServerVersion', 1,
            params, key=True)
