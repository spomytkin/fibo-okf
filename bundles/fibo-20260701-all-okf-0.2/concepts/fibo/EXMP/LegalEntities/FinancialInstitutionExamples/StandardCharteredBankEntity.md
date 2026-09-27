---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: Standard Chartered Bank entity
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: Standard Chartered Bank legal entity that is an unregistered company in the United Kingdom
  - predicate: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/LEIEntities/hasLegalFormAbbreviation
    value: Unregistered Company (en), Q0M5
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/hasLegalName
    value: Standard Chartered Bank
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/CorporateBodies/Corporation
  related_to:
  - concept: /concepts/fibo/EXMP/LegalEntities/FinancialInstitutionExamples/StandardCharteredBankHeadquartersAddress.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/FormalBusinessOrganizations/hasHeadquartersAddress
    resource: https://spec.edmcouncil.org/fibo/ontology/EXMP/LegalEntities/FinancialInstitutionExamples/StandardCharteredBankHeadquartersAddress
  - concept: /concepts/fibo/EXMP/LegalEntities/FinancialInstitutionExamples/StandardCharteredBankLegalAddress.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/LEIEntities/hasLegalAddress
    resource: https://spec.edmcouncil.org/fibo/ontology/EXMP/LegalEntities/FinancialInstitutionExamples/StandardCharteredBankLegalAddress
resource: https://spec.edmcouncil.org/fibo/ontology/EXMP/LegalEntities/FinancialInstitutionExamples/StandardCharteredBankEntity
sources:
- id: fibo-source-6ff400fc7d
  resource: references/fibo/EXMP/LegalEntities/FinancialInstitutionExamples.rdf
  sha256: 6ff400fc7d0d754db2229aaf69c84fc1cd792e55a497f9e3299ad0a0c42433f7
  title: FIBO source EXMP/LegalEntities/FinancialInstitutionExamples.rdf
title: Standard Chartered Bank entity
type: Ontology Individual
---

# Standard Chartered Bank entity

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/EXMP/LegalEntities/FinancialInstitutionExamples/StandardCharteredBankEntity>

## Definition

Standard Chartered Bank legal entity that is an unregistered company in the United Kingdom

## Relationships

- **Related to**: [StandardCharteredBankHeadquartersAddress](/concepts/fibo/EXMP/LegalEntities/FinancialInstitutionExamples/StandardCharteredBankHeadquartersAddress.md)
- **Related to**: [StandardCharteredBankLegalAddress](/concepts/fibo/EXMP/LegalEntities/FinancialInstitutionExamples/StandardCharteredBankLegalAddress.md)

## Annotations

- **label**: Standard Chartered Bank entity
- **definition**: Standard Chartered Bank legal entity that is an unregistered company in the United Kingdom
- **hasLegalFormAbbreviation**: Unregistered Company (en), Q0M5
- **hasLegalName**: Standard Chartered Bank

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
