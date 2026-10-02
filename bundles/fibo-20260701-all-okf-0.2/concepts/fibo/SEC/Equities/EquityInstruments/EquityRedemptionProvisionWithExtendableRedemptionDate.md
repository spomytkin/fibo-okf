---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: equity redemption provision with extendable redemption date
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: equity redemption provision that allows modification of the redemption date beyond the original specified date
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - kind: has_value
    property: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/hasExtendableRedemptionDate
    value: 'true'
  subclass_of:
  - concept: /concepts/fibo/SEC/Equities/EquityInstruments/EquityRedemptionProvision.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/EquityRedemptionProvision
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/EquityRedemptionProvisionWithExtendableRedemptionDate
sources:
- id: fibo-source-1c0f41de59
  resource: references/fibo/SEC/Equities/EquityInstruments.rdf
  sha256: 1c0f41de59ed514a1c80cfea5fbe96be6493eea8266f851de2d3bbd414fdcd32
  title: FIBO source SEC/Equities/EquityInstruments.rdf
title: equity redemption provision with extendable redemption date
type: Ontology Class
---

# equity redemption provision with extendable redemption date

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/EquityRedemptionProvisionWithExtendableRedemptionDate>

## Definition

equity redemption provision that allows modification of the redemption date beyond the original specified date

## Relationships

- **Subclass of**: [EquityRedemptionProvision](/concepts/fibo/SEC/Equities/EquityInstruments/EquityRedemptionProvision.md)

## Constraints

- **[hasExtendableRedemptionDate](/concepts/fibo/SEC/Equities/EquityInstruments/hasExtendableRedemptionDate.md)**: has value value `true`

## Annotations

- **label** (en): equity redemption provision with extendable redemption date
- **definition** (en): equity redemption provision that allows modification of the redemption date beyond the original specified date

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
