---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: major swap participant
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: financial service provider that maintains a substantial position in swaps for any of the major swap categories
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/abbreviation
    value: MSP
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: http://www.cftc.gov/IndustryOversight/Intermediaries/index.htm
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: This excludes positions held for hedging or mitigating commercial risk and positions maintained by an employee
      benefit plan for the primary purpose of hedging or mitigating any risk directly associated with the operation of the
      plan.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/FBC/FunctionalEntities/FinancialServicesEntities/NonDepositoryInstitution.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/FinancialServicesEntities/NonDepositoryInstitution
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Swaps/MajorSwapParticipant
sources:
- id: fibo-source-d5b3b6ccbc
  resource: references/fibo/DER/DerivativesContracts/Swaps.rdf
  sha256: d5b3b6ccbce15ed5522f2c15fde90c8b79ec7a3de33e9b48a80f97f106582966
  title: FIBO source DER/DerivativesContracts/Swaps.rdf
title: major swap participant
type: Ontology Class
---

# major swap participant

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Swaps/MajorSwapParticipant>

## Definition

financial service provider that maintains a substantial position in swaps for any of the major swap categories

## Relationships

- **Subclass of**: [NonDepositoryInstitution](/concepts/fibo/FBC/FunctionalEntities/FinancialServicesEntities/NonDepositoryInstitution.md)

## Annotations

- **label**: major swap participant
- **definition**: financial service provider that maintains a substantial position in swaps for any of the major swap categories
- **abbreviation**: MSP
- **adaptedFrom**: http://www.cftc.gov/IndustryOversight/Intermediaries/index.htm
- **explanatoryNote**: This excludes positions held for hedging or mitigating commercial risk and positions maintained by an employee benefit plan for the primary purpose of hedging or mitigating any risk directly associated with the operation of the plan.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
