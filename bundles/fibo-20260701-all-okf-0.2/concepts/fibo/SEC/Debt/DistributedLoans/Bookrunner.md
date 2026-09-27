---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: bookrunner
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: financial institution (typically a commercial or investment bank) responsible for coordinating the arrangement,
      structuring, and marketing of the loan to potential lenders
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: A 'bookrunner' is primarily responsible for managing the distribution and sale of a security during a new issuance,
      while a 'lead arranger' is the primary bank that structures and leads a syndicated loan, often assigning portions of
      the loan to other banks to participate in the deal; essentially, the bookrunner focuses on selling the security to investors,
      while the lead arranger focuses on structuring the loan itself and coordinating the syndicate of lenders involved.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/FBC/FunctionalEntities/FinancialServicesEntities/FinancialInstitution.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/FinancialServicesEntities/FinancialInstitution
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/DistributedLoans/Bookrunner
sources:
- id: fibo-source-e5c52f2c6a
  resource: references/fibo/SEC/Debt/DistributedLoans.rdf
  sha256: e5c52f2c6a506f223eaf08eee9562afee227c14cccfe925edbce3b2eeaa074b0
  title: FIBO source SEC/Debt/DistributedLoans.rdf
title: bookrunner
type: Ontology Class
---

# bookrunner

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/DistributedLoans/Bookrunner>

## Definition

financial institution (typically a commercial or investment bank) responsible for coordinating the arrangement, structuring, and marketing of the loan to potential lenders

## Relationships

- **Subclass of**: [FinancialInstitution](/concepts/fibo/FBC/FunctionalEntities/FinancialServicesEntities/FinancialInstitution.md)

## Annotations

- **label** (en): bookrunner
- **definition** (en): financial institution (typically a commercial or investment bank) responsible for coordinating the arrangement, structuring, and marketing of the loan to potential lenders
- **explanatoryNote** (en): A 'bookrunner' is primarily responsible for managing the distribution and sale of a security during a new issuance, while a 'lead arranger' is the primary bank that structures and leads a syndicated loan, often assigning portions of the loan to other banks to participate in the deal; essentially, the bookrunner focuses on selling the security to investors, while the lead arranger focuses on structuring the loan itself and coordinating the syndicate of lenders involved.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
