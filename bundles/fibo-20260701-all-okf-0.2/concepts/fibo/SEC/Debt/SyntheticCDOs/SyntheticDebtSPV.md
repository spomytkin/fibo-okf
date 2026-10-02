---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: synthetic debt s p v
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: A Special Purpose Vehicle set up for the issuance of synthetics CDOs. This entity (like all SPVs) its itself registered
      as some kind of legal entity, distinct from the sponsoring organization. It becomes the Issuer of Synthetic CDO issues.
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#editorialNote
    value: 'REVIEW: Whether this is (or is ever) a separate SPV for Synthetics, as it is for Cash CDO and other Cash structured
      finance. If not, how to define the facts at the level of SPV without contradictions. Moving stuff off the balance sheet
      is involved in putting it into the SPV. So talking a bout balance sheet or off balanc sheet, this is about creating
      the pool which is going to be sold off. This applies whether hte pool is cash (real holdings) or synthetics. Either
      way ,the instruments are transferred into the CPV to sell them off. conclusion: applies to cash and non cash. In the
      old days there were all sorts of guarantees added to that SPOV. Now if you provide support to that =SPV it is no longer
      "Off balance sheet" froma regulatory point of view. Accounting rules refer.'
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/SyntheticCDOs/SyntheticDebtInstrumentPoolFundingAsset
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/SyntheticCDOs/holds
  subclass_of:
  - concept: /concepts/fibo/BE/LegalEntities/LegalPersons/SpecialPurposeVehicle.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/LegalPersons/SpecialPurposeVehicle
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/SyntheticCDOs/SyntheticDebtSPV
sources:
- id: fibo-source-141b3c40ed
  resource: references/fibo/SEC/Debt/SyntheticCDOs.rdf
  sha256: 141b3c40ed364214aed3965d9cbe9daaa58da12da50f05938bd6d436aad71e2b
  title: FIBO source SEC/Debt/SyntheticCDOs.rdf
title: synthetic debt s p v
type: Ontology Class
---

# synthetic debt s p v

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/SyntheticCDOs/SyntheticDebtSPV>

## Definition

A Special Purpose Vehicle set up for the issuance of synthetics CDOs. This entity (like all SPVs) its itself registered as some kind of legal entity, distinct from the sponsoring organization. It becomes the Issuer of Synthetic CDO issues.

## Relationships

- **Subclass of**: [SpecialPurposeVehicle](/concepts/fibo/BE/LegalEntities/LegalPersons/SpecialPurposeVehicle.md)

## Constraints

- **[holds](/concepts/fibo/SEC/Debt/SyntheticCDOs/holds.md)**: some values from of type [SyntheticDebtInstrumentPoolFundingAsset](/concepts/fibo/SEC/Debt/SyntheticCDOs/SyntheticDebtInstrumentPoolFundingAsset.md)

## Annotations

- **label** (en): synthetic debt s p v
- **definition** (en): A Special Purpose Vehicle set up for the issuance of synthetics CDOs. This entity (like all SPVs) its itself registered as some kind of legal entity, distinct from the sponsoring organization. It becomes the Issuer of Synthetic CDO issues.
- **editorialNote** (en): REVIEW: Whether this is (or is ever) a separate SPV for Synthetics, as it is for Cash CDO and other Cash structured finance. If not, how to define the facts at the level of SPV without contradictions. Moving stuff off the balance sheet is involved in putting it into the SPV. So talking a bout balance sheet or off balanc sheet, this is about creating the pool which is going to be sold off. This applies whether hte pool is cash (real holdings) or synthetics. Either way ,the instruments are transferred into the CPV to sell them off. conclusion: applies to cash and non cash. In the old days there were all sorts of guarantees added to that SPOV. Now if you provide support to that =SPV it is no longer "Off balance sheet" froma regulatory point of view. Accounting rules refer.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
