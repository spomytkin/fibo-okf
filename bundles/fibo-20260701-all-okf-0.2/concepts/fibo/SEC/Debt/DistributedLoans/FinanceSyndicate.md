---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: finance syndicate
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: group of financial institutions or lenders that collectively agree to provide funding for a large loan to a single
      borrower
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Syndicates are formed to enable the provision of substantial financing amounts that would be challenging or risky
      for any one lender to offer alone. The syndicate structure allows lenders to share the loan amount, spreading both the
      funding and associated risks among multiple participants.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/BE/FunctionalEntities/FunctionalEntities/Syndicate.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/FunctionalEntities/FunctionalEntities/Syndicate
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/DistributedLoans/FinanceSyndicate
sources:
- id: fibo-source-e5c52f2c6a
  resource: references/fibo/SEC/Debt/DistributedLoans.rdf
  sha256: e5c52f2c6a506f223eaf08eee9562afee227c14cccfe925edbce3b2eeaa074b0
  title: FIBO source SEC/Debt/DistributedLoans.rdf
title: finance syndicate
type: Ontology Class
---

# finance syndicate

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/DistributedLoans/FinanceSyndicate>

## Definition

group of financial institutions or lenders that collectively agree to provide funding for a large loan to a single borrower

## Relationships

- **Subclass of**: [Syndicate](/concepts/fibo/BE/FunctionalEntities/FunctionalEntities/Syndicate.md)

## Annotations

- **label** (en): finance syndicate
- **definition** (en): group of financial institutions or lenders that collectively agree to provide funding for a large loan to a single borrower
- **explanatoryNote** (en): Syndicates are formed to enable the provision of substantial financing amounts that would be challenging or risky for any one lender to offer alone. The syndicate structure allows lenders to share the loan amount, spreading both the funding and associated risks among multiple participants.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
