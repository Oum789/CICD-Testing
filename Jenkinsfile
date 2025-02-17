pipeline{
    agent {label 'vm1'}
    stages{
        stage('Checkout') {
            steps {
                cleanWs() // ล้าง workspace ก่อน
                checkout scm
            }
        }
        stage('Test!') {
            steps {
                build(job: 'vm2 pipeline')
            }
        }
        stage('Pre-Prod!') {
            steps {
                build(job: 'vm3 pipeline')
            }
        }
    }
}