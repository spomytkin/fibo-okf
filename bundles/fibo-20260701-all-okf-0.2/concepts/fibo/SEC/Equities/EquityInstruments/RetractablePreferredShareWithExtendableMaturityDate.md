---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: retractable preferred share with extendable maturity date
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: retractable preferred share with a fixed maturity date whose issuer and/or holders have the option to extend the
      maturity date
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/ExtensionProvision
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/hasExtensionProvision
  - kind: has_value
    property: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/hasExtendableMaturityDate
    value: 'true'
  - kind: has_value
    property: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/hasExtendableMaturityDate
    value: 'true'
  subclass_of:
  - concept: /concepts/fibo/SEC/Equities/EquityInstruments/PreferredShareWithFixedMaturityDate.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/PreferredShareWithFixedMaturityDate
  - concept: /concepts/fibo/SEC/Equities/EquityInstruments/RetractablePreferredShare.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/RetractablePreferredShare
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/RetractablePreferredShareWithExtendableMaturityDate
sources:
- id: fibo-source-1c0f41de59
  resource: references/fibo/SEC/Equities/EquityInstruments.rdf
  sha256: 1c0f41de59ed514a1c80cfea5fbe96be6493eea8266f851de2d3bbd414fdcd32
  title: FIBO source SEC/Equities/EquityInstruments.rdf
title: retractable preferred share with extendable maturity date
type: Ontology Class
---

# retractable preferred share with extendable maturity date

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/RetractablePreferredShareWithExtendableMaturityDate>

## Definition

retractable preferred share with a fixed maturity date whose issuer and/or holders have the option to extend the maturity date

## Relationships

- **Subclass of**: [PreferredShareWithFixedMaturityDate](/concepts/fibo/SEC/Equities/EquityInstruments/PreferredShareWithFixedMaturityDate.md)
- **Subclass of**: [RetractablePreferredShare](/concepts/fibo/SEC/Equities/EquityInstruments/RetractablePreferredShare.md)

## Constraints

- **[hasExtensionProvision](/concepts/fibo/FND/Agreements/Contracts/hasExtensionProvision.md)**: some values from of type [ExtensionProvision](/concepts/fibo/FND/Agreements/Contracts/ExtensionProvision.md)
- **[hasExtendableMaturityDate](/concepts/fibo/SEC/Equities/EquityInstruments/hasExtendableMaturityDate.md)**: has value value `true`
- **[hasExtendableMaturityDate](/concepts/fibo/SEC/Equities/EquityInstruments/hasExtendableMaturityDate.md)**: has value value `true`

## Annotations

- **label**: retractable preferred share with extendable maturity date
- **definition**: retractable preferred share with a fixed maturity date whose issuer and/or holders have the option to extend the maturity date

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
