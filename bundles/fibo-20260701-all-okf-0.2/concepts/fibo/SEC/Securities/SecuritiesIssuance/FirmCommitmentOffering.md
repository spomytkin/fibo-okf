---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: firm commitment offering
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: securities offering whereby the underwriter purchases the securities outright for their own account
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: Barron's Dictionary of Finance and Investment Terms, Ninth Edition, 2014.
  disjoint_with:
  - concept: /concepts/fibo/SEC/Securities/SecuritiesIssuance/BestEffortsOffering.md
    predicate: http://www.w3.org/2002/07/owl#disjointWith
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIssuance/BestEffortsOffering
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/SEC/Securities/SecuritiesIssuance/SecuritiesOffering.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIssuance/SecuritiesOffering
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIssuance/FirmCommitmentOffering
sources:
- id: fibo-source-7b3088e831
  resource: references/fibo/SEC/Securities/SecuritiesIssuance.rdf
  sha256: 7b3088e8315beedb43222e345522bb546f87fbbd6850833103c9ba84ea1d7ac0
  title: FIBO source SEC/Securities/SecuritiesIssuance.rdf
title: firm commitment offering
type: Ontology Class
---

# firm commitment offering

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIssuance/FirmCommitmentOffering>

## Definition

securities offering whereby the underwriter purchases the securities outright for their own account

## Relationships

- **Subclass of**: [SecuritiesOffering](/concepts/fibo/SEC/Securities/SecuritiesIssuance/SecuritiesOffering.md)

## Constraints

- **Disjoint with**: [BestEffortsOffering](/concepts/fibo/SEC/Securities/SecuritiesIssuance/BestEffortsOffering.md)

## Annotations

- **label**: firm commitment offering
- **definition**: securities offering whereby the underwriter purchases the securities outright for their own account
- **adaptedFrom**: Barron's Dictionary of Finance and Investment Terms, Ninth Edition, 2014.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
