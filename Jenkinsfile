node {
    checkout scm

    stage("Build Image") {
        sh("arm build")
    }

    stage("Unit Test") {
        sh("arm unit")
    }

    stage("Publish Pipelines") {
        sh("arm pipelines \$(pwd)/pipelines")
    }

    if (env.BRANCH_NAME == "master") {
        stage("Push Image & Deb Package") {
            sh '''
              . /mnt/secrets/bintray/bintray
              arm push
            '''
        }
    }

    stage("Archive Artifacts") {
           archiveArtifacts artifacts: 'build/distributions/*.deb', fingerprint: true
    }

}
