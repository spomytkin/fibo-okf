---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: underwriter takedown
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: Infomation on Takedown quantity of the security handled by the underwriter (that will be brought into DTC).
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#editorialNote
    value: 'Question: Do securities issued through processes other than the one formally identified as "Underwriting Process",
      have Underwriters? Our research would indicate that agency and non agency MBS issuance processes are not "Underwriting"
      processes as defined for the DTCC Muni unwriting process, but they do have a step which involves identifying and appointing
      an underwriter, so the issue is underwritten. It may be that these two processes should be defined as types of (variants
      on) a more general Underwriting Process, which is itself more general than the one captured separately for DTCC Muni
      Issuance, which is where this term now lives. Modeling Note: Definition is too DTC specific, from DTCC earliy reviews
      on Muni process. Need to have a global definition and understanding of this term.'
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/DebtIssuance/MuniIssueUnderwriter
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/IssuanceProcess/takenDownBy
  - cardinality: 1
    filler: http://www.w3.org/2001/XMLSchema#integer
    kind: max_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/IssuanceProcess/underwriterTakedownShares
  subclass_of:
  - concept: /concepts/fibo/BP/SecuritiesIssuance/IssuanceProcess/UnderwritingProcessDetails.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/IssuanceProcess/UnderwritingProcessDetails
resource: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/IssuanceProcess/UnderwriterTakedown
sources:
- id: fibo-source-fa20b53ed2
  resource: references/fibo/BP/SecuritiesIssuance/IssuanceProcess.rdf
  sha256: fa20b53ed283631237b4ff106a6a421d47c8e9bcb760277569287fb0cabdce1f
  title: FIBO source BP/SecuritiesIssuance/IssuanceProcess.rdf
title: underwriter takedown
type: Ontology Class
---

# underwriter takedown

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/IssuanceProcess/UnderwriterTakedown>

## Definition

Infomation on Takedown quantity of the security handled by the underwriter (that will be brought into DTC).

## Relationships

- **Subclass of**: [UnderwritingProcessDetails](/concepts/fibo/BP/SecuritiesIssuance/IssuanceProcess/UnderwritingProcessDetails.md)

## Constraints

- **[takenDownBy](/concepts/fibo/BP/SecuritiesIssuance/IssuanceProcess/takenDownBy.md)**: some values from of type [MuniIssueUnderwriter](/concepts/fibo/BP/SecuritiesIssuance/DebtIssuance/MuniIssueUnderwriter.md)
- **[underwriterTakedownShares](/concepts/fibo/BP/SecuritiesIssuance/IssuanceProcess/underwriterTakedownShares.md)**: max qualified cardinality 1 of type [integer](<http://www.w3.org/2001/XMLSchema#integer>)

## Annotations

- **label** (en): underwriter takedown
- **definition** (en): Infomation on Takedown quantity of the security handled by the underwriter (that will be brought into DTC).
- **editorialNote** (en): Question: Do securities issued through processes other than the one formally identified as "Underwriting Process", have Underwriters? Our research would indicate that agency and non agency MBS issuance processes are not "Underwriting" processes as defined for the DTCC Muni unwriting process, but they do have a step which involves identifying and appointing an underwriter, so the issue is underwritten. It may be that these two processes should be defined as types of (variants on) a more general Underwriting Process, which is itself more general than the one captured separately for DTCC Muni Issuance, which is where this term now lives. Modeling Note: Definition is too DTC specific, from DTCC earliy reviews on Muni process. Need to have a global definition and understanding of this term.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
