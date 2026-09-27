---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: securities underwriting issuance process
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: The process by which debt instruments are offered to the market by a syndicate of underwriters who underwrite the
      issue.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/MuniIssuance/IssuanceAgent
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/MuniIssuance/hasAgent
  - filler: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/MuniIssuance/IssuanceFinancialAdvisor
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/MuniIssuance/hasFinancialAdvisor
  - filler: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/MuniIssuance/IssuerCounsel
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/MuniIssuance/hasIssuerCounsel
  - filler: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/MuniIssuance/Obligor
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/MuniIssuance/hasObligor
  - filler: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/MuniIssuance/PayingAgent
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/MuniIssuance/hasPayingAgent
  - filler: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/MuniIssuance/IssuancePrinter
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/MuniIssuance/hasPrinter
  - filler: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/MuniIssuance/RemarketingAgent
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/MuniIssuance/hasRemarketingAgent
  - filler: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/MuniIssuance/Servicer
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/MuniIssuance/hasServicer
  - filler: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/IssuanceProcess/Subscriber
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/MuniIssuance/hasSubscriber
  - filler: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/MuniIssuance/TransferAgent
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/MuniIssuance/hasTransferAgent
  - filler: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/MuniIssuance/Trustee
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/MuniIssuance/hasTrustee
  - filler: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/IssuanceProcess/UnderwritingProcessDetails
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/MuniIssuance/produces
  - filler: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/MuniIssuance/UnderwritingIssuanceRequestor
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/MuniIssuance/requestedBy
  - filler: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/MuniIssuance/PotentialMuniUnderwriter
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/MuniIssuance/underwrittenBy
  subclass_of:
  - concept: /concepts/fibo/BP/SecuritiesIssuance/IssuanceProcess/SecuritiesIssuanceProcess.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/IssuanceProcess/SecuritiesIssuanceProcess
resource: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/MuniIssuance/SecuritiesUnderwritingIssuanceProcess
sources:
- id: fibo-source-1c106070e5
  resource: references/fibo/BP/SecuritiesIssuance/MuniIssuance.rdf
  sha256: 1c106070e511dce04ec6498cc5a5df3f6dba9e882ef25649d5ada289a93e628f
  title: FIBO source BP/SecuritiesIssuance/MuniIssuance.rdf
title: securities underwriting issuance process
type: Ontology Class
---

# securities underwriting issuance process

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/MuniIssuance/SecuritiesUnderwritingIssuanceProcess>

## Definition

The process by which debt instruments are offered to the market by a syndicate of underwriters who underwrite the issue.

## Relationships

- **Subclass of**: [SecuritiesIssuanceProcess](/concepts/fibo/BP/SecuritiesIssuance/IssuanceProcess/SecuritiesIssuanceProcess.md)

## Constraints

- **[hasAgent](/concepts/fibo/BP/SecuritiesIssuance/MuniIssuance/hasAgent.md)**: some values from of type [IssuanceAgent](/concepts/fibo/BP/SecuritiesIssuance/MuniIssuance/IssuanceAgent.md)
- **[hasFinancialAdvisor](/concepts/fibo/BP/SecuritiesIssuance/MuniIssuance/hasFinancialAdvisor.md)**: some values from of type [IssuanceFinancialAdvisor](/concepts/fibo/BP/SecuritiesIssuance/MuniIssuance/IssuanceFinancialAdvisor.md)
- **[hasIssuerCounsel](/concepts/fibo/BP/SecuritiesIssuance/MuniIssuance/hasIssuerCounsel.md)**: some values from of type [IssuerCounsel](/concepts/fibo/BP/SecuritiesIssuance/MuniIssuance/IssuerCounsel.md)
- **[hasObligor](/concepts/fibo/BP/SecuritiesIssuance/MuniIssuance/hasObligor.md)**: some values from of type [Obligor](/concepts/fibo/BP/SecuritiesIssuance/MuniIssuance/Obligor.md)
- **[hasPayingAgent](/concepts/fibo/BP/SecuritiesIssuance/MuniIssuance/hasPayingAgent.md)**: some values from of type [PayingAgent](/concepts/fibo/BP/SecuritiesIssuance/MuniIssuance/PayingAgent.md)
- **[hasPrinter](/concepts/fibo/BP/SecuritiesIssuance/MuniIssuance/hasPrinter.md)**: some values from of type [IssuancePrinter](/concepts/fibo/BP/SecuritiesIssuance/MuniIssuance/IssuancePrinter.md)
- **[hasRemarketingAgent](/concepts/fibo/BP/SecuritiesIssuance/MuniIssuance/hasRemarketingAgent.md)**: some values from of type [RemarketingAgent](/concepts/fibo/BP/SecuritiesIssuance/MuniIssuance/RemarketingAgent.md)
- **[hasServicer](/concepts/fibo/BP/SecuritiesIssuance/MuniIssuance/hasServicer.md)**: some values from of type [Servicer](/concepts/fibo/BP/SecuritiesIssuance/MuniIssuance/Servicer.md)
- **[hasSubscriber](/concepts/fibo/BP/SecuritiesIssuance/MuniIssuance/hasSubscriber.md)**: some values from of type [Subscriber](/concepts/fibo/BP/SecuritiesIssuance/IssuanceProcess/Subscriber.md)
- **[hasTransferAgent](/concepts/fibo/BP/SecuritiesIssuance/MuniIssuance/hasTransferAgent.md)**: some values from of type [TransferAgent](/concepts/fibo/BP/SecuritiesIssuance/MuniIssuance/TransferAgent.md)
- **[hasTrustee](/concepts/fibo/BP/SecuritiesIssuance/MuniIssuance/hasTrustee.md)**: some values from of type [Trustee](/concepts/fibo/BP/SecuritiesIssuance/MuniIssuance/Trustee.md)
- **[produces](/concepts/fibo/BP/SecuritiesIssuance/MuniIssuance/produces.md)**: some values from of type [UnderwritingProcessDetails](/concepts/fibo/BP/SecuritiesIssuance/IssuanceProcess/UnderwritingProcessDetails.md)
- **[requestedBy](/concepts/fibo/BP/SecuritiesIssuance/MuniIssuance/requestedBy.md)**: some values from of type [UnderwritingIssuanceRequestor](/concepts/fibo/BP/SecuritiesIssuance/MuniIssuance/UnderwritingIssuanceRequestor.md)
- **[underwrittenBy](/concepts/fibo/BP/SecuritiesIssuance/MuniIssuance/underwrittenBy.md)**: some values from of type [PotentialMuniUnderwriter](/concepts/fibo/BP/SecuritiesIssuance/MuniIssuance/PotentialMuniUnderwriter.md)

## Annotations

- **label** (en): securities underwriting issuance process
- **definition** (en): The process by which debt instruments are offered to the market by a syndicate of underwriters who underwrite the issue.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
