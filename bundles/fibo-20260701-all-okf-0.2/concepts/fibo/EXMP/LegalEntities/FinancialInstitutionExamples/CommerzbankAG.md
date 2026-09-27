---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: Commerzbank AG
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: Commerzbank Aktiengesellschaft legal entity that is a stock corporation in Germany
  - language: de
    predicate: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/LEIEntities/hasLegalFormAbbreviation
    value: Aktiengesellschaft, 6QQB
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/hasLegalName
    value: Commerzbank AG
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/CorporateBodies/StockCorporation
  related_to:
  - concept: /concepts/fibo/EXMP/LegalEntities/FinancialInstitutionExamples/CommerzbankAGHeadquartersAddress.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/FormalBusinessOrganizations/hasHeadquartersAddress
    resource: https://spec.edmcouncil.org/fibo/ontology/EXMP/LegalEntities/FinancialInstitutionExamples/CommerzbankAGHeadquartersAddress
  - concept: /concepts/fibo/EXMP/LegalEntities/FinancialInstitutionExamples/CommerzbankAGLegalAddress.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/LEIEntities/hasLegalAddress
    resource: https://spec.edmcouncil.org/fibo/ontology/EXMP/LegalEntities/FinancialInstitutionExamples/CommerzbankAGLegalAddress
resource: https://spec.edmcouncil.org/fibo/ontology/EXMP/LegalEntities/FinancialInstitutionExamples/CommerzbankAG
sources:
- id: fibo-source-6ff400fc7d
  resource: references/fibo/EXMP/LegalEntities/FinancialInstitutionExamples.rdf
  sha256: 6ff400fc7d0d754db2229aaf69c84fc1cd792e55a497f9e3299ad0a0c42433f7
  title: FIBO source EXMP/LegalEntities/FinancialInstitutionExamples.rdf
title: Commerzbank AG
type: Ontology Individual
---

# Commerzbank AG

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/EXMP/LegalEntities/FinancialInstitutionExamples/CommerzbankAG>

## Definition

Commerzbank Aktiengesellschaft legal entity that is a stock corporation in Germany

## Relationships

- **Related to**: [CommerzbankAGHeadquartersAddress](/concepts/fibo/EXMP/LegalEntities/FinancialInstitutionExamples/CommerzbankAGHeadquartersAddress.md)
- **Related to**: [CommerzbankAGLegalAddress](/concepts/fibo/EXMP/LegalEntities/FinancialInstitutionExamples/CommerzbankAGLegalAddress.md)

## Annotations

- **label**: Commerzbank AG
- **definition**: Commerzbank Aktiengesellschaft legal entity that is a stock corporation in Germany
- **hasLegalFormAbbreviation** (de): Aktiengesellschaft, 6QQB
- **hasLegalName**: Commerzbank AG

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
