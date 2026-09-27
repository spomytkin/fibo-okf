---
owl:
  annotations:
  - language: fr
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: Société Générale entité
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: Société Générale legal entity that is a public limited company with a board of directors
  - language: fr
    predicate: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/LEIEntities/hasLegalFormAbbreviation
    value: SA à conseil d'administration (s.a.i.) (fr), K65D
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/hasLegalName
    value: Société Générale
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/CorporateBodies/Corporation
  related_to:
  - concept: /concepts/fibo/EXMP/LegalEntities/FinancialInstitutionExamples/SocieteGeneraleHeadquartersAddress.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/FormalBusinessOrganizations/hasHeadquartersAddress
    resource: https://spec.edmcouncil.org/fibo/ontology/EXMP/LegalEntities/FinancialInstitutionExamples/SocieteGeneraleHeadquartersAddress
  - concept: /concepts/fibo/EXMP/LegalEntities/FinancialInstitutionExamples/SocieteGeneraleLegalAddress.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/LEIEntities/hasLegalAddress
    resource: https://spec.edmcouncil.org/fibo/ontology/EXMP/LegalEntities/FinancialInstitutionExamples/SocieteGeneraleLegalAddress
resource: https://spec.edmcouncil.org/fibo/ontology/EXMP/LegalEntities/FinancialInstitutionExamples/SocieteGeneraleEntity
sources:
- id: fibo-source-6ff400fc7d
  resource: references/fibo/EXMP/LegalEntities/FinancialInstitutionExamples.rdf
  sha256: 6ff400fc7d0d754db2229aaf69c84fc1cd792e55a497f9e3299ad0a0c42433f7
  title: FIBO source EXMP/LegalEntities/FinancialInstitutionExamples.rdf
title: Société Générale entité
type: Ontology Individual
---

# Société Générale entité

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/EXMP/LegalEntities/FinancialInstitutionExamples/SocieteGeneraleEntity>

## Definition

Société Générale legal entity that is a public limited company with a board of directors

## Relationships

- **Related to**: [SocieteGeneraleHeadquartersAddress](/concepts/fibo/EXMP/LegalEntities/FinancialInstitutionExamples/SocieteGeneraleHeadquartersAddress.md)
- **Related to**: [SocieteGeneraleLegalAddress](/concepts/fibo/EXMP/LegalEntities/FinancialInstitutionExamples/SocieteGeneraleLegalAddress.md)

## Annotations

- **label** (fr): Société Générale entité
- **definition**: Société Générale legal entity that is a public limited company with a board of directors
- **hasLegalFormAbbreviation** (fr): SA à conseil d'administration (s.a.i.) (fr), K65D
- **hasLegalName**: Société Générale

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
