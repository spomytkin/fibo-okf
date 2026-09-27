---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: offering
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: The process step of offering a security for issue. This is the making available of a new securities issue through
      an underwriting.
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: It is assumed that this exists for all security types as the precise issuance process is defined among the Offering
      terms. Terms which only exist for specific types of instrument are given as specialized variants of this class of Thing.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/IssuanceProcess/SecurityOfferingDistributionMethod
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/IssuanceProcess/hasDistributionType
  - filler: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/IssuanceProcess/SecurityOfferingSaleMethod
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/IssuanceProcess/hasSaleMethod
  - filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIssuance/OfferingDocument
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/IssuanceProcess/requiredToMakeEligible
  - filler: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/IssuanceProcess/IssuedSecurityIssueInformation
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/MuniIssuance/givesRiseTo
  subclass_of:
  - concept: /concepts/fibo/BP/SecuritiesIssuance/DebtIssuance/IssuanceProcessActivity.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/DebtIssuance/IssuanceProcessActivity
resource: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/IssuanceProcess/OfferingProcess
sources:
- id: fibo-source-fa20b53ed2
  resource: references/fibo/BP/SecuritiesIssuance/IssuanceProcess.rdf
  sha256: fa20b53ed283631237b4ff106a6a421d47c8e9bcb760277569287fb0cabdce1f
  title: FIBO source BP/SecuritiesIssuance/IssuanceProcess.rdf
title: offering
type: Ontology Class
---

# offering

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/IssuanceProcess/OfferingProcess>

## Definition

The process step of offering a security for issue. This is the making available of a new securities issue through an underwriting.

## Relationships

- **Subclass of**: [IssuanceProcessActivity](/concepts/fibo/BP/SecuritiesIssuance/DebtIssuance/IssuanceProcessActivity.md)

## Constraints

- **[hasDistributionType](/concepts/fibo/BP/SecuritiesIssuance/IssuanceProcess/hasDistributionType.md)**: some values from of type [SecurityOfferingDistributionMethod](/concepts/fibo/BP/SecuritiesIssuance/IssuanceProcess/SecurityOfferingDistributionMethod.md)
- **[hasSaleMethod](/concepts/fibo/BP/SecuritiesIssuance/IssuanceProcess/hasSaleMethod.md)**: some values from of type [SecurityOfferingSaleMethod](/concepts/fibo/BP/SecuritiesIssuance/IssuanceProcess/SecurityOfferingSaleMethod.md)
- **[requiredToMakeEligible](/concepts/fibo/BP/SecuritiesIssuance/IssuanceProcess/requiredToMakeEligible.md)**: some values from of type [OfferingDocument](/concepts/fibo/SEC/Securities/SecuritiesIssuance/OfferingDocument.md)
- **[givesRiseTo](/concepts/fibo/BP/SecuritiesIssuance/MuniIssuance/givesRiseTo.md)**: some values from of type [IssuedSecurityIssueInformation](/concepts/fibo/BP/SecuritiesIssuance/IssuanceProcess/IssuedSecurityIssueInformation.md)

## Annotations

- **label** (en): offering
- **definition** (en): The process step of offering a security for issue. This is the making available of a new securities issue through an underwriting.
- **explanatoryNote** (en): It is assumed that this exists for all security types as the precise issuance process is defined among the Offering terms. Terms which only exist for specific types of instrument are given as specialized variants of this class of Thing.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
