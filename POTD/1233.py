def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()

        result = []

        result.append(folder[0])

        for i in range(1,len(folder)):
            currFolder = folder[i]
            lastFolder = result[-1]
            lastFolder += "/"

            # Only add if currFolder is NOT a subfolder of lastFolder
            if not currFolder.startswith(lastFolder):
                result.append(currFolder)


        return result