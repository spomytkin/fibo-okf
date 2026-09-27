---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: fund subscription terms
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: 'Subscription terms for the fund. Further notes: ISO FIBIM, EFAMA DD and FPP combine terms for subscription, redemption
      and general holding requirements. These have been separated here as they are different kinds of term, but this can be
      reviewed. Subscription Terms are identified as terms of the fund and not the fund unit, since terms for how you might
      subscribe can''t be binding one someone who has not yet subscribed.'
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/Funds/FundUnit
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/ContextualDesignators/appliesTo
  subclass_of:
  - concept: /concepts/fibo/SEC/Funds/CollectiveInvestmentVehicles/FundProcessingTerms.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/CollectiveInvestmentVehicles/FundProcessingTerms
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/CollectiveInvestmentVehicles/FundSubscriptionTerms
sources:
- id: fibo-source-ee709790f7
  resource: references/fibo/SEC/Funds/CollectiveInvestmentVehicles.rdf
  sha256: ee709790f7157eacba64b78b55ac3e69da45c99673be17ca2df35d4f0ed3230c
  title: FIBO source SEC/Funds/CollectiveInvestmentVehicles.rdf
title: fund subscription terms
type: Ontology Class
---

# fund subscription terms

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/CollectiveInvestmentVehicles/FundSubscriptionTerms>

## Definition

Subscription terms for the fund. Further notes: ISO FIBIM, EFAMA DD and FPP combine terms for subscription, redemption and general holding requirements. These have been separated here as they are different kinds of term, but this can be reviewed. Subscription Terms are identified as terms of the fund and not the fund unit, since terms for how you might subscribe can't be binding one someone who has not yet subscribed.

## Relationships

- **Subclass of**: [FundProcessingTerms](/concepts/fibo/SEC/Funds/CollectiveInvestmentVehicles/FundProcessingTerms.md)

## Constraints

- **[appliesTo](<https://www.omg.org/spec/Commons/ContextualDesignators/appliesTo>)**: some values from of type [FundUnit](/concepts/fibo/SEC/Funds/Funds/FundUnit.md)

## Annotations

- **label** (en): fund subscription terms
- **definition** (en): Subscription terms for the fund. Further notes: ISO FIBIM, EFAMA DD and FPP combine terms for subscription, redemption and general holding requirements. These have been separated here as they are different kinds of term, but this can be reviewed. Subscription Terms are identified as terms of the fund and not the fund unit, since terms for how you might subscribe can't be binding one someone who has not yet subscribed.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
