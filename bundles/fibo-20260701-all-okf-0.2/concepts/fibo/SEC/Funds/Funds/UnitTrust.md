---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: unit trust
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: pooled investment vehicle in which investors hold units that represent beneficial ownership in a trust-managed
      portfolio of assets
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: A unit trust is established under a trust deed, with a trustee holding legal title to the assets and a fund manager
      making investment decisions. They are common in the UK, Australia, Singapore, and other Commonwealth countries.
  disjoint_with:
  - concept: /concepts/fibo/SEC/Funds/Funds/MutualFund.md
    predicate: http://www.w3.org/2002/07/owl#disjointWith
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/Funds/MutualFund
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/SEC/Funds/Funds/UnitizedFund.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/Funds/UnitizedFund
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/Funds/UnitTrust
sources:
- id: fibo-source-a82c11f42e
  resource: references/fibo/SEC/Funds/Funds.rdf
  sha256: a82c11f42ef79a0f83aeae8434ad054ddef746da9d97126ef3d8923eacf9c275
  title: FIBO source SEC/Funds/Funds.rdf
title: unit trust
type: Ontology Class
---

# unit trust

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/Funds/UnitTrust>

## Definition

pooled investment vehicle in which investors hold units that represent beneficial ownership in a trust-managed portfolio of assets

## Relationships

- **Subclass of**: [UnitizedFund](/concepts/fibo/SEC/Funds/Funds/UnitizedFund.md)

## Constraints

- **Disjoint with**: [MutualFund](/concepts/fibo/SEC/Funds/Funds/MutualFund.md)

## Annotations

- **label** (en): unit trust
- **definition** (en): pooled investment vehicle in which investors hold units that represent beneficial ownership in a trust-managed portfolio of assets
- **explanatoryNote** (en): A unit trust is established under a trust deed, with a trustee holding legal title to the assets and a fund manager making investment decisions. They are common in the UK, Australia, Singapore, and other Commonwealth countries.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
