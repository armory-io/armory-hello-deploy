node {
    checkout scm

    stage("Build Image") {
        sh("arm build")
    }

    stage("Build Image") {
        sh("arm unit")
    }

    stage("Build Image") {
        sh '''
          . /mnt/secrets/bintray/bintray
          arm push
        '''
    }

}
