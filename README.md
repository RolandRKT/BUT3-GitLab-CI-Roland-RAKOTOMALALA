Roland RAKOTOMALALA

Premier readme

[![CI](https://github.com/RolandRKT/BUT3-GitLab-CI-Roland-RAKOTOMALALA/actions/workflows/ci.yml/badge.svg)](https://github.com/RolandRKT/BUT3-GitLab-CI-Roland-RAKOTOMALALA/actions/workflows/ci.yml)

Reussite du build - Fin de la partie 2.

Je note que :

`export PYTHONPATH=$(pwd)/src ; pytest --cov --cov-report=term-missing --cov-config=.coveragerc`
&
`export PYTHONPATH=$(pwd)/src ; pytest --cov --cov-report=term-missing`

font la même chose. Le coveragerc semble récupérer automatiquement le `.coverage`.