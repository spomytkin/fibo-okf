---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: redeemable preferred share with extendable redemption date
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: redeemable preferred share whose redemption date can be modified
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: extendible preferred share
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/EquityRedemptionProvisionWithExtendableRedemptionDate
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/hasExtensionProvision
  subclass_of:
  - concept: /concepts/fibo/SEC/Equities/EquityInstruments/RedeemablePreferredShare.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/RedeemablePreferredShare
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/RedeemablePreferredShareWithExtendableRedemptionDate
sources:
- id: fibo-source-1c0f41de59
  resource: references/fibo/SEC/Equities/EquityInstruments.rdf
  sha256: 1c0f41de59ed514a1c80cfea5fbe96be6493eea8266f851de2d3bbd414fdcd32
  title: FIBO source SEC/Equities/EquityInstruments.rdf
title: redeemable preferred share with extendable redemption date
type: Ontology Class
---

# redeemable preferred share with extendable redemption date

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/RedeemablePreferredShareWithExtendableRedemptionDate>

## Definition

redeemable preferred share whose redemption date can be modified

## Relationships

- **Subclass of**: [RedeemablePreferredShare](/concepts/fibo/SEC/Equities/EquityInstruments/RedeemablePreferredShare.md)

## Constraints

- **[hasExtensionProvision](/concepts/fibo/FND/Agreements/Contracts/hasExtensionProvision.md)**: some values from of type [EquityRedemptionProvisionWithExtendableRedemptionDate](/concepts/fibo/SEC/Equities/EquityInstruments/EquityRedemptionProvisionWithExtendableRedemptionDate.md)

## Annotations

- **label**: redeemable preferred share with extendable redemption date
- **definition**: redeemable preferred share whose redemption date can be modified
- **synonym**: extendible preferred share

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
