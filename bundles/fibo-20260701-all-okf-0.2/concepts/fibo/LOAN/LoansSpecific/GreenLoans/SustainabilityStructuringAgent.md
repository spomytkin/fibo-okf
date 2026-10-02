---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: sustainability structuring agent
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: financial institution appointed to help design, implement, and monitor the sustainability aspects of a syndicated
      green loan
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: This role is typically present in sustainability-linked loans (SLLs) or green loans, which tie the loan's terms
      to the borrower's environmental, social, and governance (ESG) performance. The sustainability structuring agent's role
      is crucial in ensuring that the loan's sustainability metrics align with both the borrower's goals and the expectations
      of the participating lenders.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/BE/FunctionalEntities/FunctionalEntities/SyndicateMember.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/FunctionalEntities/FunctionalEntities/SyndicateMember
resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/GreenLoans/SustainabilityStructuringAgent
sources:
- id: fibo-source-cff1f078be
  resource: references/fibo/LOAN/LoansSpecific/GreenLoans.rdf
  sha256: cff1f078bed4eeb9970073ab5ccbace470a24c6150ac1e18310cbe1894b9e006
  title: FIBO source LOAN/LoansSpecific/GreenLoans.rdf
title: sustainability structuring agent
type: Ontology Class
---

# sustainability structuring agent

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/GreenLoans/SustainabilityStructuringAgent>

## Definition

financial institution appointed to help design, implement, and monitor the sustainability aspects of a syndicated green loan

## Relationships

- **Subclass of**: [SyndicateMember](/concepts/fibo/BE/FunctionalEntities/FunctionalEntities/SyndicateMember.md)

## Annotations

- **label** (en): sustainability structuring agent
- **definition** (en): financial institution appointed to help design, implement, and monitor the sustainability aspects of a syndicated green loan
- **explanatoryNote** (en): This role is typically present in sustainability-linked loans (SLLs) or green loans, which tie the loan's terms to the borrower's environmental, social, and governance (ESG) performance. The sustainability structuring agent's role is crucial in ensuring that the loan's sustainability metrics align with both the borrower's goals and the expectations of the participating lenders.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
