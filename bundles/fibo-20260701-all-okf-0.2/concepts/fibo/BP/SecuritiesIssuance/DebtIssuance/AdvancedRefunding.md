---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: advance refunding
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: refunding in which bond issuance in which new bonds are sold at a lower rate than outstanding ones
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: The proceeds are then invested, and when the older bonds become callable they are paid off with the invested proceeds.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/BP/SecuritiesIssuance/DebtIssuance/RefundingPurpose.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/DebtIssuance/RefundingPurpose
resource: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/DebtIssuance/AdvancedRefunding
sources:
- id: fibo-source-560fdfbe3a
  resource: references/fibo/BP/SecuritiesIssuance/DebtIssuance.rdf
  sha256: 560fdfbe3abab0e0bb6f417a8acec1661acf530aeee87d8a033ef11bbf4af57b
  title: FIBO source BP/SecuritiesIssuance/DebtIssuance.rdf
title: advance refunding
type: Ontology Class
---

# advance refunding

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/DebtIssuance/AdvancedRefunding>

## Definition

refunding in which bond issuance in which new bonds are sold at a lower rate than outstanding ones

## Relationships

- **Subclass of**: [RefundingPurpose](/concepts/fibo/BP/SecuritiesIssuance/DebtIssuance/RefundingPurpose.md)

## Annotations

- **label** (en): advance refunding
- **definition** (en): refunding in which bond issuance in which new bonds are sold at a lower rate than outstanding ones
- **explanatoryNote** (en): The proceeds are then invested, and when the older bonds become callable they are paid off with the invested proceeds.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
