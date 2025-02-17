pipeline{
    agent none
    stages{
        stage('Test') {
            steps {
                build(job: 'vm2 pipeline')
            }
        }
        stage('Pre-Prod') {
            steps {
                build(job: 'vm3 pipeline')
            }
        }
    }
}