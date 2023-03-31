class ResourcePool:
    def __init__(self) -> None:
        self._available = []  # create an empty stack to hold available resources
        self._allocated = []  # create an empty stack to hold allocated resources

    def get_resource(self):
        if not self._available:  # check if available stack is empty
            result = Resource(None)  # create a new resource if no resource is available
        else:
            result = self._available.pop()  # get a resource from the available stack
        self._allocated.append(result)  # add the resource to the allocated stack
        return result

class Resource:
    def __init__(self, value=None) -> None:
        self.value = value

    def setvalue(self, value):
        self.value = value

def main():
    pool = ResourcePool()
    resource = pool.get_resource()
    resource.setvalue(5)
    print(resource.value)

if __name__ == "__main__":
    main()
