node {
    checkout scm

    stage("Build Image") {
        sh("arm build")
    }

    stage("Unit Test") {
        sh("arm unit")
    }

    stage("Push Image & Deb Package") {
        sh '''
          . /mnt/secrets/bintray/bintray
          arm push
        '''
    }

}
