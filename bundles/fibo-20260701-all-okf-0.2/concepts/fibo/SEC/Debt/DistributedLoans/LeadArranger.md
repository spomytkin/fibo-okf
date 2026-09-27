---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: lead arranger
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: financial institution that spearheads the loan structuring and syndication process on behalf of the borrower
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: The lead arranger acts as the primary point of contact for the borrower. They perform credit analysis and due diligence,
      ensure that the structure meets borrowers goals, and coordinates with potential lenders regarding the initial structure
      and commitments.
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: arranger
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: lead bank
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: lead manager
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/FBC/FunctionalEntities/FinancialServicesEntities/FinancialInstitution.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/FinancialServicesEntities/FinancialInstitution
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/DistributedLoans/LeadArranger
sources:
- id: fibo-source-e5c52f2c6a
  resource: references/fibo/SEC/Debt/DistributedLoans.rdf
  sha256: e5c52f2c6a506f223eaf08eee9562afee227c14cccfe925edbce3b2eeaa074b0
  title: FIBO source SEC/Debt/DistributedLoans.rdf
title: lead arranger
type: Ontology Class
---

# lead arranger

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/DistributedLoans/LeadArranger>

## Definition

financial institution that spearheads the loan structuring and syndication process on behalf of the borrower

## Relationships

- **Subclass of**: [FinancialInstitution](/concepts/fibo/FBC/FunctionalEntities/FinancialServicesEntities/FinancialInstitution.md)

## Annotations

- **label** (en): lead arranger
- **definition** (en): financial institution that spearheads the loan structuring and syndication process on behalf of the borrower
- **explanatoryNote** (en): The lead arranger acts as the primary point of contact for the borrower. They perform credit analysis and due diligence, ensure that the structure meets borrowers goals, and coordinates with potential lenders regarding the initial structure and commitments.
- **synonym** (en): arranger
- **synonym** (en): lead bank
- **synonym** (en): lead manager

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
