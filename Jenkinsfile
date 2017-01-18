node {
    checkout scm

    stage("Build Image") {
        sh("arm build")
    }

    stage("Build Image") {
        sh '''
          source /mnt/secrets/bintray
          arm push
        '''
    }

}
