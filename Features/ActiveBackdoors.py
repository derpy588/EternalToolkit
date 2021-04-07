from Features.base import FeatureBase


class Feature(FeatureBase):
    def __init__(self):
        super().__init__(
            name="Active Backdoors",
            description="This will get you all active backdoors that are running on a PC.",
            options=[]
        )

    def function(self, options):
        print("Coming Soon")
        input('Press any key to return to main screen.')