=========================================================
7. Your solution should include a README explaining how to build and run the application with Docker. We will follow the steps you provide in readme file and execute it to verify.

a. run these cmd @ terminal

docker build -t hi_walmart

docker run -d hi_walmart -p 8080:8080

b. click http://localhost:8080/healthz

http://localhost:8080/

=========================================================

1. What other information would you add to health endpoint json object in step 2? 
    Explain what would be the use case for that extra information?
    a.  dataBase : mySQL, MongoDB. 
    b.  hardware info: RAM,CPU, SSD, netWork, GPU. 
    c.  Custom Health Indicator.
     
2. How would you automate the build/test/deploy process for this application? (a verbal answer is enough. installation of CICD is bonus, not required)
    a. Set up a build server +  test suites for CICD

3. What branching strategy would you use for development?
    a. Feature Branching :allow developers to create 1 branch for 1 feature=user stories, it allows 9 developers to work separately.
    b. Release Branching =  1 branch for a release that includes all user stories in 1 team.

5. What CICD tool/service would you use?
    a. TeamCity because I use IntelliJ,Jenkins,CircleCI

6. What stages would you have in the CICD pipeline?
What would be the purpose of each stage in CICD pipeline?
    1. build= developers put in their code and then again code goes to the version control system having a proper version tag. If we have a code and it needs to be compiled before execution. So, through the version control phase, it again goes to build phase where it gets compiled. You get all the features of that code from various branches of the repository, which merge them and finally use a compiler to compile it. 
    2. unit test= we have various kinds of testing, 1 of them is  unit test 
    3. deploy =deploy it into a staging or a test server. Here, you can view the code or you can view the app in a simulator.
    4. Integration Test=Once the code is deployed successfully, you can run another set of a sanity test. If everything is accepted, then it can be deployed to production.
    5.Deploy to Production= Meanwhile in every step, if there is some error, you can shoot a mail back to dev so that they can fix them. Then they will push it into the version control system and goes back into the pipeline.Once again if there is any error reported during testing, again the feedback goes to the dev team where they fix it and the process re-iterates if required.
    6. Measure+Validate = So, this lifecycle continues until we get a code which can be deployed in the production server where we measure and validate the code.


