---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: identify conforming mortgage
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: Identify mortgage conforming to overall requirements for this issuer.
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: This does not relate to the criteria for belonging to an individual, defined mortgage pool but conforms to the
      requirements of the issuing organization overall. This is for Agency pools. For non-agency, the equivalent of this step
      is carried out at pool level with a clause to reject the mortgage.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/LOAN/RealEstateLoans/Mortgages/LoanSecuredByRealEstate
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Documents/refersTo
  subclass_of:
  - concept: /concepts/fibo/BP/SecuritiesIssuance/IssuanceProcess/IssuanceProcessActivity.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/IssuanceProcess/IssuanceProcessActivity
resource: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/AgencyMBSIssuance/IdentifyConformingMortgage
sources:
- id: fibo-source-2eeca2019d
  resource: references/fibo/BP/SecuritiesIssuance/AgencyMBSIssuance.rdf
  sha256: 2eeca2019d428c47ac1513eaf8db629142182da83295878f53a62e84592f6a59
  title: FIBO source BP/SecuritiesIssuance/AgencyMBSIssuance.rdf
title: identify conforming mortgage
type: Ontology Class
---

# identify conforming mortgage

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/AgencyMBSIssuance/IdentifyConformingMortgage>

## Definition

Identify mortgage conforming to overall requirements for this issuer.

## Relationships

- **Subclass of**: [IssuanceProcessActivity](/concepts/fibo/BP/SecuritiesIssuance/IssuanceProcess/IssuanceProcessActivity.md)

## Constraints

- **[refersTo](<https://www.omg.org/spec/Commons/Documents/refersTo>)**: some values from of type [LoanSecuredByRealEstate](/concepts/fibo/LOAN/RealEstateLoans/Mortgages/LoanSecuredByRealEstate.md)

## Annotations

- **label** (en): identify conforming mortgage
- **definition** (en): Identify mortgage conforming to overall requirements for this issuer.
- **explanatoryNote** (en): This does not relate to the criteria for belonging to an individual, defined mortgage pool but conforms to the requirements of the issuing organization overall. This is for Agency pools. For non-agency, the equivalent of this step is carried out at pool level with a clause to reject the mortgage.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
