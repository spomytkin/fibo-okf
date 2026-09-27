---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: bond offering with warrant
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: 'a bond offering where the issue includes a warrant; Further notes: ISO 10962 CFI definition is A bond that is
      issued together with one or more warrant(s) attached as part of the offer, the warrant(s) granting the holder the right
      to purchase a designated security, often the common stock of the issuer of the debt, at a specified price. Review notes:
      This need not be any specific type of bond. The warrant is used as a sweetener to encourage people to subscribe to a
      new bond issue. The Bond and the Warrant trade together as a unit (called "Bond Unit").'
  disjoint_with:
  - concept: /concepts/fibo/BP/SecuritiesIssuance/DebtIssuance/MediumTermNoteOffering.md
    predicate: http://www.w3.org/2002/07/owl#disjointWith
    resource: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/DebtIssuance/MediumTermNoteOffering
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - kind: some_values_from
    property: https://www.omg.org/spec/Commons/ContextualDesignators/appliesTo
    value: N04c3d6527be94a2ea63d31405ced71b1
  subclass_of:
  - concept: /concepts/fibo/BP/SecuritiesIssuance/DebtIssuance/BondOffering.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/DebtIssuance/BondOffering
resource: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/DebtIssuance/BondOfferingWithWarrant
sources:
- id: fibo-source-560fdfbe3a
  resource: references/fibo/BP/SecuritiesIssuance/DebtIssuance.rdf
  sha256: 560fdfbe3abab0e0bb6f417a8acec1661acf530aeee87d8a033ef11bbf4af57b
  title: FIBO source BP/SecuritiesIssuance/DebtIssuance.rdf
title: bond offering with warrant
type: Ontology Class
---

# bond offering with warrant

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/DebtIssuance/BondOfferingWithWarrant>

## Definition

a bond offering where the issue includes a warrant; Further notes: ISO 10962 CFI definition is A bond that is issued together with one or more warrant(s) attached as part of the offer, the warrant(s) granting the holder the right to purchase a designated security, often the common stock of the issuer of the debt, at a specified price. Review notes: This need not be any specific type of bond. The warrant is used as a sweetener to encourage people to subscribe to a new bond issue. The Bond and the Warrant trade together as a unit (called "Bond Unit").

## Relationships

- **Subclass of**: [BondOffering](/concepts/fibo/BP/SecuritiesIssuance/DebtIssuance/BondOffering.md)

## Constraints

- **Disjoint with**: [MediumTermNoteOffering](/concepts/fibo/BP/SecuritiesIssuance/DebtIssuance/MediumTermNoteOffering.md)
- **[appliesTo](<https://www.omg.org/spec/Commons/ContextualDesignators/appliesTo>)**: some values from value `N04c3d6527be94a2ea63d31405ced71b1`

## Annotations

- **label** (en): bond offering with warrant
- **definition** (en): a bond offering where the issue includes a warrant; Further notes: ISO 10962 CFI definition is A bond that is issued together with one or more warrant(s) attached as part of the offer, the warrant(s) granting the holder the right to purchase a designated security, often the common stock of the issuer of the debt, at a specified price. Review notes: This need not be any specific type of bond. The warrant is used as a sweetener to encourage people to subscribe to a new bond issue. The Bond and the Warrant trade together as a unit (called "Bond Unit").

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
