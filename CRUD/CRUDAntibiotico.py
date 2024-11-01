from modelo.antibioticos import Antibiotico

class CRUDAntibiotico:
    #7 productos de antibióticos
    @staticmethod
    def create():
        antibiotico1=Antibiotico("antibiotico1",300,"caprinos",87000)
        antibiotico2=Antibiotico("antibiotico2porcinos",500,"porcinos",256000)
        antibiotico3=Antibiotico("antibiotico3porcinos",500,"porcinos",340000)
        antibiotico4=Antibiotico("antibiotico4bovi",400,"bovinos",540000)
        antibiotico5=Antibiotico("antibiotico5bovinos",800,"bovinos",750000)
        antibiotico6=Antibiotico("antibiotico6prembovinos",600,"bovinos",640000)
        antibiotico7=Antibiotico("antibiotico7litebovinos",800,"bovinos",950000)
        
        return [antibiotico1,antibiotico2,antibiotico3,antibiotico4,antibiotico5,antibiotico6,antibiotico7]