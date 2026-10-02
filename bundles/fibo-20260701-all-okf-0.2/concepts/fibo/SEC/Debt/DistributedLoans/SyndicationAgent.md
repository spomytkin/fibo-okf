---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: syndication agent
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: financial institution (typically a commercial or investment bank) designated to help structure, arrange, and manage
      the loan syndication process
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Syndication agents are important at the beginning of the process, including setting up the syndicate, supporting
      distribution of the loan across lenders, marketing, and the like. They are far less involved in loan administration,
      which is managed by the administrative agent.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/FBC/FunctionalEntities/FinancialServicesEntities/FinancialInstitution.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/FinancialServicesEntities/FinancialInstitution
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/DistributedLoans/SyndicationAgent
sources:
- id: fibo-source-e5c52f2c6a
  resource: references/fibo/SEC/Debt/DistributedLoans.rdf
  sha256: e5c52f2c6a506f223eaf08eee9562afee227c14cccfe925edbce3b2eeaa074b0
  title: FIBO source SEC/Debt/DistributedLoans.rdf
title: syndication agent
type: Ontology Class
---

# syndication agent

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/DistributedLoans/SyndicationAgent>

## Definition

financial institution (typically a commercial or investment bank) designated to help structure, arrange, and manage the loan syndication process

## Relationships

- **Subclass of**: [FinancialInstitution](/concepts/fibo/FBC/FunctionalEntities/FinancialServicesEntities/FinancialInstitution.md)

## Annotations

- **label** (en): syndication agent
- **definition** (en): financial institution (typically a commercial or investment bank) designated to help structure, arrange, and manage the loan syndication process
- **explanatoryNote** (en): Syndication agents are important at the beginning of the process, including setting up the syndicate, supporting distribution of the loan across lenders, marketing, and the like. They are far less involved in loan administration, which is managed by the administrative agent.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
